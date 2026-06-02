---
topic: 量化部署
parent: 数据与API
tags: [data, API, financial, 2025]
created: 2026-06-02
---

# 金融数据API全面汇总（2025）

> [!note] 概述
> 2025年主流的金融数据API接口汇总，覆盖A股、美股、港股、加密货币及另类数据源。

## 国内数据源

### 免费

| 数据源 | 资产覆盖 | 数据类型 | 特点 |
|--------|---------|---------|------|
| **akshare** | A股、港股、期货、基金、债券 | 历史+实时 | 最全免费库，社区活跃 |
| **Tushare** | A股、期货、指数 | 历史 | 老牌数据API，需积分 |
| **baostock** | A股 | 历史 | 轻量级，无需注册 |

### 付费

| 数据源 | 资产覆盖 | 数据深度 | 价格区间 |
|--------|---------|---------|---------|
| **JQData**（聚宽） | A股全量 | Tick/分钟/日线/财务 | 中 |
| **Wind** | 全球多资产 | 全维度 | 高 |
| **Choice**（东方财富） | A股、基金 | 日线/财务 | 中 |
| **RiceQuant**（米筐） | A股 | 日线/分钟/因子 | 中 |

## 海外数据源

### 免费

| 数据源 | 资产覆盖 | 数据类型 |
|--------|---------|---------|
| **yfinance** | 美股、ETF、全球指数 | 历史日线/分钟线 |
| **Alpha Vantage** | 美股、加密货币 | 历史+实时（免费额度有限） |
| **FRED**（美联储） | 宏观经济 | 经济指标 |
| **Quandl** | 多种资产 | 部分免费数据集 |

### 付费（专业级）

| 数据源 | 特点 | 适合 |
|--------|------|------|
| **Polygon.io** | 机构级低延迟、完整退市覆盖 | 专业机构 |
| **TickDB** | 多资产统一接口、夜盘数据 | 全球配置团队 |
| **Alpaca** | 免费额度高、适合学习 | 个人开发者 |
| **Bloomberg** | 全球最全 | 顶级机构 |
| **CRSP** | 学术级退市数据 | 学术研究 |

## 数据源对比（美股）

| 维度 | Polygon.io | TickDB | Alpaca |
|------|-----------|--------|--------|
| 历史长度 | 10-20年+ | 近10年 | 免费10年1分钟线 |
| 退市覆盖 | 付费版完整 | 覆盖广泛 | 主要为当前存活 |
| 全球资产 | 美股为主 | 6大市场 | 美股为主 |
| 夜盘数据 | 支持 | 支持 | 有限 |
| 核心优势 | 机构级低延迟 | 多资产统一接口 | 免费额度高 |

## API接入示例

### yfinance
```python
import yfinance as yf
msft = yf.Ticker("MSFT")
hist = msft.history(period="1y")
```

### akshare
```python
import akshare as ak
df = ak.stock_zh_a_hist(
    symbol="000001",
    period="daily",
    start_date="20200101",
    end_date="20231231"
)
```

### Polygon.io
```python
import requests
url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-01/2023-12-31"
params = {"apiKey": "YOUR_KEY"}
resp = requests.get(url, params=params).json()
```

## 数据频率对比

| 频率 | 适合策略 | 数据量/天 | 延迟 |
|------|---------|---------|------|
| 日线 | 中低频选股 | KB | T+1 |
| 1分钟 | 日内交易 | ~10MB | 秒级 |
| Tick | 高频交易 | ~100MB-1GB | 毫秒级 |
| L2盘口 | 做市/HFT | ~GB+ | <1ms |

## 选择建议

- **个人学习**：akshare + yfinance（免费，覆盖广）
- **A股研究**：JQData或akshare
- **美股量化团队**：Polygon.io（专业）或 Alpaca（入门）
- **多资产全球配置**：TickDB（统一接口）
- **学术研究**：CRSP + Compustat
