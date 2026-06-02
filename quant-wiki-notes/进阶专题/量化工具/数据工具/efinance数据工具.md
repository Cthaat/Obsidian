---
title: efinance数据工具
description: 免费开源Python金融数据获取库，支持股票、基金、期货、可转债数据
tags: [数据工具, Python, efinance, 股票数据, 基金数据, 期货数据]
source: https://efinance.readthedocs.io/en/latest/
created: 2026-06-02
aliases: []
updated: 2026-06-02
---

# efinance数据工具

> [!note] 工具概览
> `efinance` 是由个人打造的免费开源 Python 库，用于获取**股票、基金、期货、可转债**数据。支持 A 股、美股及 ETF，提供 K 线行情、实时报价、龙虎榜、资金流向、季报数据等丰富接口。仅供学习交流使用。

## 基本信息

- **GitHub**: [Micro-sheep/efinance](https://github.com/Micro-sheep/efinance)
- **文档**: [efinance.readthedocs.io](https://efinance.readthedocs.io)
- **Python版本**: 3.6+
- **安装**: `pip install efinance`
- **替代数据源**: [TickFlow](https://tickflow.org)（限流时备用）

## 核心模块

| 模块 | 功能 | 典型方法 |
|------|------|----------|
| `ef.stock` | 股票数据 | `get_quote_history()`, `get_realtime_quotes()` |
| `ef.fund` | 基金数据 | `get_quote_history()`, `get_invest_position()` |
| `ef.bond` | 可转债数据 | `get_realtime_quotes()`, `get_all_base_info()` |
| `ef.futures` | 期货数据 | `get_futures_base_info()` |

## 股票数据接口

### K线历史行情

支持日K、周K、月K及分钟K线，可指定频率参数 `klt`：

```python
import efinance as ef

# 日K线
ef.stock.get_quote_history('600519')

# 5分钟K线
ef.stock.get_quote_history('600519', klt=5)

# 美股（支持代码或名称）
ef.stock.get_quote_history('AAPL')
ef.stock.get_quote_history('微软')

# ETF
ef.stock.get_quote_history('513050')
```

**返回字段**: 股票名称、股票代码、日期、开盘、收盘、最高、最低、成交量、成交额、振幅、涨跌幅、涨跌额、换手率

### 实时行情报价

```python
# 沪深A股全部实时行情
ef.stock.get_realtime_quotes()
```

**返回字段**: 股票代码、股票名称、涨跌幅、最新价、最高、最低、今开、涨跌额、换手率、量比、动态市盈率、成交量、成交额、昨日收盘、总市值、流通市值、行情ID、市场类型

### 龙虎榜数据

```python
# 最新龙虎榜
ef.stock.get_daily_billboard()

# 指定日期区间
ef.stock.get_daily_billboard(start_date='2021-08-20', end_date='2021-08-27')
```

**返回字段**: 股票代码、股票名称、上榜日期、解读、收盘价、涨跌幅、换手率、龙虎榜净买额/买入额/卖出额/成交额、市场总成交额、净买额占比、流通市值、上榜原因

### 资金流向

```python
# 日级资金流向
ef.stock.get_history_bill('300750')

# 分钟级当日资金流向
ef.stock.get_today_bill('300750')
```

**返回字段**: 主力净流入、小单净流入、中单净流入、大单净流入、超大单净流入（含占比）

### 季度财报表现

```python
# 全市场A股季度表现
ef.stock.get_all_company_performance()
```

**返回字段**: 股票代码、股票简称、公告日期、营业收入、营收同比/环比、净利润、净利润同比/环比、每股收益、每股净资产、净资产收益率、销售毛利率、每股经营现金流

## 基金数据接口

```python
# 基金历史净值
ef.fund.get_quote_history('161725')

# 基金公开持仓
ef.fund.get_invest_position('161725')

# 多只基金基本信息
ef.fund.get_base_info(['161725', '005827'])
```

**净值字段**: 日期、单位净值、累计净值、涨跌幅
**持仓字段**: 基金代码、股票代码、股票简称、持仓占比、较上期变化、公开日期

## 可转债数据接口

```python
# 可转债实时行情
ef.bond.get_realtime_quotes()

# 全部可转债基础信息
ef.bond.get_all_base_info()

# 指定可转债K线
ef.bond.get_quote_history('123111')
```

**基础信息字段**: 债券代码、债券名称、正股代码、正股名称、债券评级、申购日期、发行规模、中签率、上市日期、到期日期、期限、利率说明

## 期货数据接口

```python
# 交易所期货基本信息
ef.futures.get_futures_base_info()
```

**覆盖交易所**: 郑商所、大商所、中金所、上海能源期货交易所等

## 使用场景

1. **量化回测数据源**: 获取历史K线用于策略回测
2. **龙虎榜监控**: 追踪游资和机构席位动向
3. **资金流向分析**: 主力资金日级/分钟级流向
4. **基金持仓研究**: 追踪公募基金季度调仓
5. **可转债筛选**: 全市场可转债信息查询

## 与其他数据工具对比

| 特性 | efinance | [[目录|AKShare]] | [[目录|TuShare]] |
|------|----------|-----|---------|
| 费用 | 免费 | 免费 | 部分免费 |
| 数据源 | 东方财富 | 多源聚合 | 多源 |
| 安装难度 | 低 | 低 | 中 |
| API Key | 不需要 | 不需要 | 需要 |

## 相关笔记

- [[AKShare数据工具]]
- [[量化数据源]]
- [[TuShare数据接口]]
- [[Python量化环境配置]]

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
