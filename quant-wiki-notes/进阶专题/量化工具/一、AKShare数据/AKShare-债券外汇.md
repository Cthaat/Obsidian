---
title: AKShare 债券外汇
tags: [AKShare, 债券, 外汇, 数据接口]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/bond/bond.md (~101 KB), fx/fx.md (~22 KB)
parent: "[[AKShare概览]]"
---

# AKShare 债券外汇

> [!note] 概述
> 债券数据来自中国外汇交易中心（全国银行间同业拆借中心），外汇数据来自东方财富行情中心。

## 一、债券数据

### 债券基础名词

| 名词 | 说明 |
|------|------|
| 固定收益证券 | 持券人可在特定时间内取得固定收益 |
| 国债 | 国家以其信用为基础发行的债券，最安全的投资工具 |
| 可转债 | 在一定条件下可转换为股票的债券 |
| 短期融资券 | 期限在1年以内的债券 |
| 中期票据 | 期限在1-10年的债券 |

### 核心债券接口

| 接口名称 | 数据源 | 功能描述 |
|---------|--------|---------|
| `bond_info_cm(...)` | 中国外汇交易中心 | 债券信息查询（可按名称/代码/类型/评级筛选） |
| `bond_info_detail_cm(symbol)` | 中国外汇交易中心 | 债券详情（含64个字段的完整信息） |
| `bond_cb_jsl(cookie)` | 集思录 | 可转债数据 |
| `bond_cb_redeem_jsl()` | 集思录 | 可转债强赎数据 |
| `bond_zh_us_rate(start_date)` | 东方财富 | 中国-美国债券收益率对比 |

**示例 — 债券查询**：
```python
import akshare as ak

# 查询短期融资券
bond_info_cm_df = ak.bond_info_cm(
    bond_name="", bond_code="",
    bond_type="短期融资券",
    coupon_type="零息式",
    issue_year="2019",
    grade="A-1",
    underwriter="重庆农村商业银行股份有限公司"
)
print(bond_info_cm_df)
# 输出: 债券简称 | 债券代码 | 发行人 | 债券类型 | 发行日期 | 评级 | 查询代码
```

**示例 — 债券详情**：
```python
bond_info_detail_cm_df = ak.bond_info_detail_cm(symbol="19万林投资CP001")
print(bond_info_detail_cm_df)
# 输出: 64 行完整债券信息（全称、代码、ISIN、评级等）
```

### 债券分类体系

AKShare 债券文档还包含完整的 **债券分类体系说明**：

- **按发行主体**：政府债券、金融债券、公司债券
- **按付息方式**：零息债券、附息债券、贴现债券
- **按偿还期限**：短期(1年内)、中期(1-10年)、长期(10年以上)
- **按募集方式**：公募债券、私募债券

## 二、外汇数据

### 核心外汇接口

| 接口名称 | 功能描述 | 数据量 |
|---------|---------|--------|
| `forex_spot_em()` | 东方财富-所有汇率-实时行情（190条） | 单次全部 |
| `forex_hist_em(symbol)` | 指定汇率的历史行情数据 | 按品种 |

**示例 — 获取外汇实时行情**：
```python
import akshare as ak

forex_spot_em_df = ak.forex_spot_em()
print(forex_spot_em_df)
# 输出: 190条汇率记录（USDZAR, HKDJPY, USDJPY, CADJPY, CNHJPY...）

# 获取美元兑离岸人民币历史数据
forex_hist_em_df = ak.forex_hist_em(symbol="USDCNH")
print(forex_hist_em_df)
# 数据区间从 2010-08-23 至今
```

## 相关笔记
- [[AKShare概览]]
- [[AKShare-期货期权]]
- [[AKShare-宏观指数]]
