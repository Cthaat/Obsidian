---
topic: 量化部署
parent: 数据与API
tags: [API, exchange, trading-platform, deployment]
created: 2026-06-02
---

# 交易所API接入实战

> [!note] 概述
> 从零搭建量化交易平台，核心环节之一是将策略与交易所API对接。本文覆盖三大交易所类型及完整的接入流程。

## 交易所API架构

```
┌──────────────────────────────────────┐
│         量化交易平台                  │
│  ┌─────────┐ ┌────────┐ ┌────────┐  │
│  │数据获取  │ │订单执行 │ │账户管理 │  │
│  └────┬─────┘ └───┬────┘ └───┬────┘  │
│       │            │           │      │
└───────┼────────────┼───────────┼──────┘
        │            │           │
   ┌────▼────────────▼───────────▼──────┐
   │           REST API                 │
   │  · 历史K线  · 下单  · 账户查询     │
   ├────────────────────────────────────┤
   │        WebSocket API               │
   │  · 实时行情  · 订单推送  · 成交    │
   └────────────────────────────────────┘
```

## 三大交易所类型

### 1. 传统券商API

| 券商 | 市场 | API类型 | 门槛 |
|------|------|---------|------|
| Interactive Brokers (IB) | 全球 | REST + TWS API | 需开户 |
| 华泰证券 | A股 | REST | 需开户 |
| 中信证券 | A股 | REST | 需开户 |
| Alpaca | 美股 | REST + WebSocket | 免费注册 |

### 2. 加密货币交易所

| 交易所 | API文档 | 费率 |
|--------|---------|------|
| Binance | REST + WebSocket | 0.1% maker/taker |
| OKX | REST + WebSocket | 0.08% maker/taker |
| Bybit | REST + WebSocket | 0.1% maker/taker |

### 3. 量化平台API

| 平台 | 特点 |
|------|------|
| 聚宽（JoinQuant） | 在线回测 + 模拟交易 + 实盘 |
| 掘金量化 | 本地SDK + 策略托管 |
| RiceQuant（米筐） | 在线回测 + 信号服务 |

## 核心API接口

### 行情数据

```python
# REST: 获取K线
GET /api/v1/klines?symbol=BTCUSDT&interval=1h&limit=100

# WebSocket: 订阅实时行情
{
    "method": "SUBSCRIBE",
    "params": ["btcusdt@kline_1m"],
    "id": 1
}
```

### 订单执行

```python
# 限价单
POST /api/v1/order
{
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "quantity": 0.01,
    "price": 50000
}

# 市价单
POST /api/v1/order
{
    "symbol": "BTCUSDT",
    "side": "SELL",
    "type": "MARKET",
    "quantity": 0.01
}
```

### 账户与风控

```python
# 查询账户
GET /api/v1/account

# 查询持仓
GET /api/v1/positions

# 查询订单状态
GET /api/v1/order?orderId=12345
```

## 安全考虑

### API密钥管理

```
最佳实践：
├── 使用环境变量存储密钥（非硬编码）
├── 设置API密钥的IP白名单
├── 只授权需要的权限（取消提现权限）
├── 定期轮换API密钥
└── 使用Read-Only Key做数据获取
```

### 风控规则

| 规则 | 实现 |
|------|------|
| 单笔限额 | 最大金额硬限制 |
| 频率限制 | 符合交易所Rate Limit |
| 撤单保护 | 超时未成交自动撤单 |
| 签名验证 | HMAC-SHA256签名 |
| 时间戳校验 | 防重放攻击 |

## Python实战架子

```python
import hmac
import hashlib
import time
import requests

class ExchangeClient:
    def __init__(self, api_key, secret_key, base_url):
        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

    def _sign(self, params):
        query_string = '&'.join([f"{k}={v}" for k,v in sorted(params.items())])
        signature = hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, symbol, side, quantity, price=None):
        params = {
            'symbol': symbol,
            'side': side,
            'type': 'LIMIT' if price else 'MARKET',
            'quantity': quantity,
            'timestamp': int(time.time() * 1000)
        }
        if price:
            params['price'] = price
        params['signature'] = self._sign(params)
        headers = {'X-API-KEY': self.api_key}
        return requests.post(
            f"{self.base_url}/api/v1/order",
            headers=headers, json=params
        ).json()
```

## 常见陷阱

- **延时**：WebSocket比REST更适合实时数据
- **Rate Limit**：超过限制会被封IP，需做请求节流
- **时间戳同步**：服务器时间与本地时间偏差会导致签名错误
- **部分成交**：必须处理部分成交的情况
- **WebSocket断连**：必须实现自动重连机制
- **API升级**：交易所API版本变更可能破坏策略
