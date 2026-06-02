---
title: AKShare 基金数据
tags: [AKShare, 基金, 公募, 私募, 数据接口]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/fund/fund_public.md, fund_private.md
parent: "[[AKShare概览]]"
---

# AKShare 基金数据

> [!note] 概述
> AKShare 覆盖**公募基金**和**私募基金**两大类数据，公募基金数据文档约 195 KB（含 5000+ 行），私募基金数据约 34 KB。

## 一、公募基金数据

### 基金基本信息

| 接口名称 | 数据源 | 功能描述 |
|---------|--------|---------|
| `fund_name_em()` | 东方财富-天天基金 | 所有基金的基本信息（代码、简称、类型、拼音） |
| `fund_info_ths(symbol)` | 同花顺 | 指定基金的基本信息（管理人、托管人、费率等） |

**示例 — 获取所有基金列表**：
```python
import akshare as ak

fund_name_em_df = ak.fund_name_em()
print(fund_name_em_df)
# 输出: 基金代码 | 拼音缩写 | 基金简称 | 基金类型 | 拼音全称
```

**示例 — 获取基金基本信息（同花顺）**：
```python
fund_info_ths_df = ak.fund_info_ths(symbol="161130")
print(fund_info_ths_df)
# 输出: 基金代码、简称、类型、基金经理、成立日期、管理费、托管费等
```

### 基金净值数据

| 接口名称 | 功能描述 |
|---------|---------|
| `fund_open_fund_info_em(symbol, indicator)` | 开放式基金净值（单位/累计净值） |
| `fund_etf_fund_info_em(symbol)` | ETF 基金实时数据 |
| `fund_lof_fund_info_em(symbol)` | LOF 基金实时数据 |

### 基金排行与筛选

| 接口名称 | 功能描述 |
|---------|---------|
| `fund_rating_all()` | 基金评级总汇 |
| `fund_rating_sh(date)` | 上海证券基金评级 |
| `fund_rating_zeq(date)` | 招商证券基金评级 |

## 二、私募基金数据

### 中国证券投资基金业协会（AMAC）

| 接口名称 | 功能描述 |
|---------|---------|
| `amac_member_info()` | 会员机构综合查询（4800+ 条记录） |
| `amac_person_fund_org_list()` | 基金从业人员资格注册信息 |
| `amac_manager_info()` | 私募基金管理人登记信息 |

### 私募产品信息

| 接口名称 | 功能描述 |
|---------|---------|
| `amac_fund_info()` | 私募基金产品备案信息 |

**示例 — 查询协会会员**：
```python
import akshare as ak

amac_member_info_df = ak.amac_member_info()
print(amac_member_info_df)
# 输出: 机构名称 | 会员代表 | 会员类型 | 会员编号 | 入会时间 | 机构类型 | 是否星标
```

## 三、基金相关名词

AKShare 文档中还包括基金分类名词解释：

| 类型 | 说明 |
|------|------|
| 开放式基金 | 基金份额总额不固定，可在交易日随时申购赎回 |
| 封闭式基金 | 基金份额在合同期限内固定不变，交易在二级市场进行 |
| ETF | 交易型开放式指数基金，可在交易所交易 |
| LOF | 上市型开放式基金，既可在交易所交易也可在网点申赎 |
| QDII | 合格境内机构投资者，可投资海外市场 |
| FOF | 基金中的基金，投资于其他基金 |

## 相关笔记
- [[AKShare概览]]
- [[AKShare-股票数据]]
