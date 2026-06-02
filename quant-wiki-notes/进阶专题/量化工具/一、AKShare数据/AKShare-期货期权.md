---
title: AKShare 期货期权
tags: [AKShare, 期货, 期权, 数据接口, CFFEX]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/futures/futures.md (~181 KB), option/option.md (~130 KB)
parent: "[[AKShare概览]]"
aliases: []
updated: 2026-06-02
---

# AKShare 期货期权

> [!note] 概述
> AKShare 覆盖国内主要期货/期权交易所的行情、基础信息和交易数据。期货文档约 181 KB，期权文档约 130 KB。

## 一、期货数据

### 期货交易所一览

| 交易所 | 代码 | 合约后缀 | 首页地址 |
|--------|------|---------|---------|
| 中国金融期货交易所 | CFFEX | .CFX | [cffex.com.cn](http://www.cffex.com.cn) |
| 上海期货交易所 | SHFE | .SHF | [shfe.com.cn](https://www.shfe.com.cn) |
| 上海国际能源交易中心 | INE | .INE | [ine.cn](https://www.ine.cn) |
| 郑州商品交易所 | CZCE | .ZCE | [czce.com.cn](http://www.czce.com.cn) |
| 大连商品交易所 | DCE | .DCE | [dce.com.cn](http://www.dce.com.cn) |
| 广州期货交易所 | GFEX | .GFEX | [gfex.com.cn](http://www.gfex.com.cn) |

### 期货交易时间

AKShare 文档中附带完整的**期货交易时间表**（更新于 2024-11-18），涵盖六大交易所所有品种的集合竞价、日盘和夜盘时间。

**示例 — 部分品种交易时间**：

| 品种 | 代码 | 日盘 | 夜盘 |
|------|------|------|------|
| 螺纹钢 | rb | 09:00-15:00（含休息） | 21:00-23:00 |
| 黄金 | au | 09:00-15:00（含休息） | 21:00-02:30 |
| 原油 | sc | 09:00-15:00（含休息） | 21:00-02:30 |
| 铁矿石 | i | 09:00-15:00（含休息） | 21:00-23:00 |
| 沪深300股指 | IF | 09:30-11:30, 13:00-15:00 | - |
| 30年期国债 | TL | 09:30-11:30, 13:00-15:15 | - |

### 核心期货接口

| 接口名称 | 功能描述 |
|---------|---------|
| `futures_main_sina(symbol)` | 新浪-主力合约行情 |
| `futures_zh_spot_em()` | 东方财富-期货实时行情 |
| `futures_zh_daily_sina(symbol)` | 新浪-期货日线数据 |
| `futures_foreign_hist(symbol)` | 外盘期货历史数据 |
| `futures_warehouse_receipt(symbol)` | 仓单日报数据 |
| `futures_open_interest_rank(symbol, date)` | 期货持仓排名 |

## 二、期权数据

### 期权交易所

| 交易所 | 代码 | 品种示例 |
|--------|------|---------|
| 中国金融期货交易所 | CFFEX | 沪深300股指期权(IO)、上证50(HO)、中证1000(MO) |
| 上海期货交易所 | SHFE | 铜/黄金/螺纹钢/原油等期权 |
| 郑州商品交易所 | CZCE | 棉花/白糖/甲醇/纯碱等期权 |
| 大连商品交易所 | DCE | 豆粕/铁矿石/棕榈油/玉米等期权 |
| 广州期货交易所 | GFEX | 工业硅/碳酸锂/多晶硅期权 |
| 上海证券交易所 | SSE | ETF 期权 |
| 深圳证券交易所 | SZSE | ETF 期权 |

### 核心期权接口

| 接口名称 | 功能描述 |
|---------|---------|
| `option_finance_board(symbol)` | 金融期权-期权行情 |
| `option_sse_list(symbol)` | 上交所-ETF期权合约列表 |
| `option_szse_list(symbol)` | 深交所-ETF期权合约列表 |
| `option_cffex_spot_sina(symbol)` | 中金所-股指期权实时行情 |
| `option_dce_daily(symbol)` | 大商所-商品期权日行情 |
| `option_czce_daily(date)` | 郑商所-商品期权日行情 |

**示例 — 上交所ETF期权合约列表**：
```python
import akshare as ak

option_sse_list_df = ak.option_sse_list(symbol="510050")
print(option_sse_list_df)
```

## 相关笔记
- [[AKShare概览]]
- [[AKShare-股票数据]]
- [[AKShare-债券外汇]]

## 课程化学习补充

> [!important] 学习定位
> 工具服务于研究闭环：获取数据、清洗数据、验证策略、执行交易和复盘监控；选择工具要看稳定性和可维护性。本文仅用于学习、研究与复盘，不构成任何投资建议。

### 必须掌握的问题

- 接口是否稳定
- 数据字段和频率是否满足策略
- 版本是否锁定
- 是否有替代数据源交叉验证

### 实战应用流程

1. 先写清楚你的投资假设：为什么这个信号、资产或方法应该产生收益。
2. 明确数据口径：样本范围、更新时间、复权/分红/停牌处理和交易日历。
3. 做最小可行验证：先用简单规则验证方向，再逐步加入复杂模型。
4. 把成本和约束前置：手续费、滑点、冲击成本、保证金、流动性和容量都要进入测算。
5. 上线后持续复盘：记录信号、下单、成交、持仓、回撤和失效原因。

### 风险与失效条件

- 免费数据缺口
- 网页结构变化导致接口失效
- 版本升级破坏兼容
- 忽视数据授权和合规

### 复盘问题

- 这笔交易或这套模型赚的是什么钱：风险补偿、行为偏差、流动性溢价，还是偶然噪音？
- 如果市场环境反过来，最大亏损和最长恢复期会是多少？
- 当前结论是否依赖某个不可持续假设，例如低利率、低波动、充裕流动性或监管套利？
- 有没有一个更简单的基准策略能取得接近效果？

### 延伸学习

- [[Python量化环境配置]]
- [[AKShare概览]]
- [[VnPy框架详解]]
- [[量化数据源]]
