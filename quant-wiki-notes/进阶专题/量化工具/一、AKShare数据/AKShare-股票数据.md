---
title: AKShare 股票数据
tags: [AKShare, 股票, 数据接口, A股, 行情]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/stock/stock.md (983 KB)
parent: "[[AKShare概览]]"
aliases: []
updated: 2026-06-02
---

# AKShare 股票数据

> [!note] 概述
> AKShare 股票数据模块是整个库中**最大的子模块**（约 983 KB），提供 A 股市场的行情数据、基本面数据、龙虎榜、融资融券等全方位数据接口。

## 核心接口分类

### 一、A股市场总貌

| 接口名称 | 功能描述 | 数据源 |
|---------|---------|--------|
| `stock_sse_summary()` | 上海证券交易所-股票数据总貌 | 上交所 |
| `stock_szse_summary(date)` | 深圳证券交易所-证券类别统计 | 深交所 |

**示例**：
```python
import akshare as ak

# 上交所总貌
stock_sse_summary_df = ak.stock_sse_summary()
print(stock_sse_summary_df)

# 深交所统计
stock_szse_summary_df = ak.stock_szse_summary(date="20200619")
print(stock_szse_summary_df)
```

### 二、A股个股数据

| 接口名称 | 功能描述 |
|---------|---------|
| `stock_zh_a_hist(symbol, period, start_date, end_date)` | A股历史行情数据（日/周/月/季/年） |
| `stock_zh_a_spot_em()` | A股实时行情数据（东方财富） |
| `stock_individual_info_em(symbol)` | 个股基本信息（公司概况） |
| `stock_individual_fund_flow(symbol, market)` | 个股资金流向 |

### 三、财务数据

| 接口名称 | 功能描述 |
|---------|---------|
| `stock_financial_abstract(symbol)` | 财务指标摘要 |
| `stock_profit_sheet_by_report_em(symbol)` | 利润表 |
| `stock_balance_sheet_by_report_em(symbol)` | 资产负债表 |
| `stock_cash_flow_sheet_by_report_em(symbol)` | 现金流量表 |
| `stock_yjkb_em(date)` | 业绩快报 |

### 四、龙虎榜数据

| 接口名称 | 功能描述 |
|---------|---------|
| `stock_lhb_detail_em(start_date, end_date)` | 龙虎榜详情 |
| `stock_lhb_hyyyb_em(start_date, end_date)` | 龙虎榜营业部统计 |
| `stock_lhb_stock_statistic_em(start_date, end_date)` | 龙虎榜个股上榜统计 |

### 五、融资融券

| 接口名称 | 功能描述 |
|---------|---------|
| `stock_margin_detail_sse(date)` | 沪市融资融券明细 |
| `stock_margin_detail_szse(date)` | 深市融资融券明细 |
| `stock_margin_sse(start_date)` | 沪市融资融券汇总 |

### 六、板块与行业

| 接口名称 | 功能描述 |
|---------|---------|
| `stock_board_concept_name_em()` | 东方财富-概念板块 |
| `stock_board_industry_name_em()` | 东方财富-行业板块 |
| `stock_board_concept_hist_em(symbol)` | 概念板块历史行情 |

## 数据接口特点

- 每个接口有明确的 **输入参数**（名称/类型/描述）和 **输出参数**（字段/类型/描述）
- 所有接口均提供可运行的 `import akshare as ak` 示例代码
- 包含真实的数据输出示例
- 标注了接口的 **限量** 说明（单次返回量级）

## 相关笔记
- [[AKShare概览]]
- [[AKShare-基金数据]]
- [[AKShare-期货期权]]

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
