---
title: Fama-French数据处理
tags:
  - Fama-French
  - 数据处理
  - 因子构建
  - 数据清洗
created: 2026-06-02
type: note
source: fama-french-data-processing.md
---

# Fama-French数据处理

> [!note] 数据处理
> Fama-French因子模型的数据处理是因子构建的关键步骤，包括数据清洗、分组和因子计算。

## 数据准备

### 所需数据
- **股票收益率**：月度收益率数据
- **市值数据**：总市值或流通市值
- **财务数据**：账面价值、营业收入、总资产
- **无风险利率**：国债收益率

### 数据来源
- Wind、Choice等国内数据终端
- CSMAR、WIND等学术数据库
- Yahoo Finance、Alpha Vantage等国际数据源

## 数据处理流程

### 1. 数据清洗
```python
# 删除缺失值
data = data.dropna(subset=['return', 'market_cap', 'book_value'])

# 排除金融股
data = data[~data['industry'].isin(['银行', '保险', '证券'])]

# 排除ST股
data = data[~data['name'].str.contains('ST')]
```

### 2. 异常值处理
```python
# Winsorize处理（缩尾处理）
from scipy.stats.mstats import winsorize
data['return'] = winsorize(data['return'], limits=[0.01, 0.01])
```

### 3. 分组构建
```python
# 2x3分组法
# 按市值中位数分为S和B
# 按B/M的30%和70%分位数分为L、M、H
```

### 4. 因子收益率计算
```python
# SMB = 1/3(SL + SM + SH) - 1/3(BL + BM + BH)
# HML = 1/2(SH + BH) - 1/2(SL + BL)
```

## 常见问题

- 数据频率不匹配
- 幸存者偏差
- 前视偏差
- 缺失值处理

## 相关链接

- [[Fama-French三因子模型]]
- [[Fama-French五因子模型]]
- [[Fama-French实战指南]]
- [[资产定价研究方法论]]
