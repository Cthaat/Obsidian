---
title: AKShare 其他数据
tags: [AKShare, 现货, 能源, 货币, 加密货币, NLP]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/spot/, energy/, currency/, hf/, nlp/, qdii/, qhkc/
parent: "[[AKShare概览]]"
aliases: []
updated: 2026-06-02
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

## 实战掌握清单

> [!tip] 交易者视角
> AKShare 其他数据 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

### 关键判断

- 确认数据源、字段含义、更新频率、限流和异常值处理。
- 检查工具是否支持复现、日志、版本管理和错误恢复。
- 把接口能力和策略需求对齐，避免为工具而工具。

### 落地动作

1. 建立数据校验、缓存、重试和缺失值报告。
2. 把研究代码、回测代码和实盘代码的差异写清楚。
3. 上线前做小资金、只读或模拟环境验证。

### 失效边界

- 接口字段变更导致结果失真。
- 缺少日志无法追踪错误。
- 把工具稳定性误认为策略有效性。

### 复盘问题

- 这项知识改变了哪一个具体决策：标的、方向、仓位、退出、对冲还是不交易？
- 如果判断相反，最大亏损、最长恢复期和退出触发条件是什么？
- 有没有一个更简单的基准方法可以取得相近结果？
