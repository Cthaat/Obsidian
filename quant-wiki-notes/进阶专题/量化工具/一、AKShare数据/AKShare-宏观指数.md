---
title: AKShare 宏观指数
tags: [AKShare, 宏观数据, 指数, 利率, 经济]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/macro/macro.md (~387 KB), index/index.md (~183 KB), interest_rate/interest_rate.md
parent: "[[AKShare概览]]"
aliases: []
updated: 2026-06-02
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
