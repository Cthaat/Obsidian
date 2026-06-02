---
title: AKShare 宏观指数
tags: [AKShare, 宏观数据, 指数, 利率, 经济]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/macro/macro.md (~387 KB), index/index.md (~183 KB), interest_rate/interest_rate.md
parent: "[[AKShare概览]]"
---

# AKShare 宏观指数

> [!note] 概述
> 宏观数据是 AKShare 第二大模块（387 KB），覆盖中国及全球宏观经济指标。指数数据约 183 KB，利率数据约 30 KB。

## 一、中国宏观数据

### 宏观杠杆率

| 接口名称 | 数据源 | 功能描述 | 数据量 |
|---------|--------|---------|--------|
| `macro_cnbs()` | 中国国家金融与发展实验室 | 中国宏观杠杆率（居民/企业/政府/金融） | 126行（1992-至今） |

**输出字段**：居民部门、非金融企业部门、政府部门、中央政府、地方政府、实体经济部门、金融部门资产方/负债方

**示例**：
```python
import akshare as ak

macro_cnbs_df = ak.macro_cnbs()
print(macro_cnbs_df)
# 最新数据显示: 实体经济部门杠杆率 ~294.8%
```

### 国民经济运行

| 接口名称 | 功能描述 |
|---------|---------|
| `macro_china_qyspjg()` | 企业商品价格指数（2005年至今） |
| `macro_china_gdp()` | 中国GDP数据 |
| `macro_china_cpi()` | 居民消费价格指数(CPI) |
| `macro_china_pmi()` | 制造业采购经理指数(PMI) |
| `macro_china_ppi()` | 工业生产者出厂价格指数(PPI) |
| `macro_china_money_supply()` | 货币供应量(M0/M1/M2) |
| `macro_china_trade_balance()` | 贸易差额 |

### 全球经济指标

| 接口名称 | 功能描述 |
|---------|---------|
| `macro_usa_gdp()` | 美国GDP |
| `macro_usa_cpi()` | 美国CPI |
| `macro_usa_non_farm()` | 美国非农就业 |
| `macro_euro_gdp()` | 欧元区GDP |

## 二、利率数据

| 接口名称 | 功能描述 | 数据区间 |
|---------|---------|---------|
| `macro_bank_usa_interest_rate()` | 美联储利率决议报告 | 1982年至今（287行） |
| `macro_bank_euro_interest_rate()` | 欧洲央行决议报告 | 1999年至今 |
| `bond_china_yield(start_date)` | 中国国债收益率曲线 | — |
| `macro_china_lpr()` | 中国贷款市场报价利率(LPR) | — |
| `macro_china_shibor(date)` | 上海银行间同业拆放利率(Shibor) | — |

## 三、指数数据

### A股指数（东方财富）

| 接口名称 | 功能描述 | 参数 |
|---------|---------|------|
| `stock_zh_index_spot_em(symbol)` | 东方财富-指数实时行情 | 可选：沪深重要/上证系列/深证系列/中证系列 |
| `stock_zh_index_daily_em(symbol)` | 指数日线数据 | 指定指数代码 |
| `stock_zh_index_value_csindex(symbol)` | 中证指数估值数据 | 如 "000300" |

**示例 — 获取上证系列指数**：
```python
import akshare as ak

stock_zh_index_spot_em_df = ak.stock_zh_index_spot_em(symbol="上证系列指数")
print(stock_zh_index_spot_em_df)
# 输出 179 条指数，含上证指数(000001)、A股指数(000002)等
```

### 全球指数

| 接口名称 | 功能描述 |
|---------|---------|
| `index_global_spot_em()` | 全球指数实时行情 |
| `index_us_stock_sina()` | 美股三大指数（道琼斯/纳斯达克/标普500） |
| `index_japan_niigata()` | 日本日经指数 |

## 相关笔记
- [[AKShare概览]]
- [[AKShare-债券外汇]]
- [[AKShare-其他数据]]
