---
title: AKShare 期货期权
tags: [AKShare, 期货, 期权, 数据接口, CFFEX]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/futures/futures.md (~181 KB), option/option.md (~130 KB)
parent: "[[AKShare概览]]"
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
