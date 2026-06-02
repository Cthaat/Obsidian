---
title: AKShare 其他数据
tags: [AKShare, 现货, 能源, 货币, 加密货币, NLP]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/spot/, energy/, currency/, hf/, nlp/, qdii/, qhkc/
parent: "[[AKShare概览]]"
---

# AKShare 其他数据

> [!note] 概述
> 除了核心的股票/基金/期货/债券/宏观数据外，AKShare 还提供现货、能源、货币、加密货币、NLP 等小众但有价值的数据模块。

## 一、现货数据

| 接口名称 | 数据源 | 功能描述 |
|---------|--------|---------|
| `spot_price_qh(symbol)` | 99期货 | 现货走势（期现价差），如"螺纹钢" |
| `spot_hist_sge(symbol)` | 上海黄金交易所 | 黄金现货历史行情，如 `Au99.99` |
| `spot_symbol_table_sge()` | 上海黄金交易所 | 可查询的品种列表 |

## 二、能源数据

| 接口名称 | 数据源 | 功能描述 |
|---------|--------|---------|
| `energy_carbon_domestic(symbol)` | 碳交易网 | 国内碳排放权行情（湖北/上海/北京/广东等） |
| `energy_carbon_bj()` | 北京碳排放权电子交易平台 | 北京碳排放权公开交易行情 |
| `energy_oil_hist()` | — | 国际原油价格历史数据 |

**示例**：
```python
import akshare as ak

# 碳排放数据
energy_carbon_domestic_df = ak.energy_carbon_domestic(symbol="湖北")
print(energy_carbon_domestic_df)
# 数据: 日期 | 成交价 | 成交量 | 成交额 | 地点
```

## 三、货币数据

| 接口名称 | 数据源 | 功能描述 | 限制 |
|---------|--------|---------|------|
| `currency_latest(base, symbols, api_key)` | CurrencyScoop | 全球货币报价最新数据 | 免费 5000次/月 |
| `currency_history(base, date, symbols, api_key)` | CurrencyScoop | 指定日期货币历史报价 | 免费 5000次/月 |

## 四、加密货币

| 接口名称 | 功能描述 |
|---------|---------|
| `crypto_js_spot()` | 加密货币实时行情（从金十数据） |

## 五、其他模块

### QDII 数据
| 接口名称 | 功能描述 |
|---------|---------|
| `qdii_hist_em(symbol)` | QDII 基金历史净值数据 |

### 期货开户云（qhkc）
| 接口名称 | 功能描述 |
|---------|---------|
| `qhkc_company_info()` | 期货公司信息查询 |

### 高频数据（hf）
| 接口名称 | 功能描述 |
|---------|---------|
| `stock_zh_a_tick_tx(symbol)` | 腾讯-股票分笔数据 |
| `stock_zh_a_tick_163(symbol)` | 网易-股票分笔数据 |

### NLP 事件数据
| 接口名称 | 功能描述 |
|---------|---------|
| `stock_zh_a_alerts_cls()` | 财联社-股市警报 |

### 文章/资讯
| 接口名称 | 数据源 | 功能描述 |
|---------|--------|---------|
| `article_zh_em()` | 东方财富 | 财经要闻/快讯 |

## 辅助工具

| 工具 | 说明 |
|------|------|
| `tool_trade_date_hist_sina()` | 历史交易日历 |
| `akshare.__version__` | 查看 AKShare 版本 |

## 相关笔记
- [[AKShare概览]]
- [[AKShare-宏观指数]]
- [[AKShare-股票数据]]
