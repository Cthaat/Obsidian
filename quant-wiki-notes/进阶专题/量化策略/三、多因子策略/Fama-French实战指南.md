---
title: Fama-French实战指南
tags:
  - Fama-French
  - Python实战
  - 因子构建
  - 回测
created: 2026-06-02
type: note
source: fama-french-practical-guide.md
---

# Fama-French实战指南

> [!note] 实战应用
> 本文介绍Fama-French因子模型的Python实战应用，包括因子构建、回归分析和投资组合构建的完整流程。

## Python实现步骤

### 1. 数据获取
```python
import pandas as pd
import numpy as np

# 获取股票数据和财务数据
# 需要：收益率、市值、账面市值比、盈利能力、投资率
```

### 2. 因子构建
```python
# 按市值分组（SMB）
median_market_cap = data['market_cap'].median()
small = data[data['market_cap'] <= median_market_cap]
big = data[data['market_cap'] > median_market_cap]

# 按B/M分组（HML）
data['BM'] = data['book_value'] / data['market_cap']
high_bm = data[data['BM'] > data['BM'].quantile(0.7)]
low_bm = data[data['BM'] < data['BM'].quantile(0.3)]
```

### 3. 回归分析
```python
import statsmodels.api as sm

# Fama-French回归
X = sm.add_constant(data[['MKT', 'SMB', 'HML', 'RMW', 'CMA']])
y = data['excess_return']
model = sm.OLS(y, X).fit()
print(model.summary())
```

### 4. 因子收益计算
```python
# 2x3分组法
def assign_portfolios(data):
    # 按市值分为小(S)和大(B)
    # 按B/M分为低(L)、中(M)、高(H)
    # 形成6个组合：SL, SM, SH, BL, BM, BH
    pass
```

## 关键注意事项

- 数据频率：月度数据最常用
- 样本选择：排除金融股、ST股
- 缺失值处理：删除或插值
- 异常值处理：Winsorize处理

## 相关链接

- [[Fama-French三因子模型]]
- [[Fama-French五因子模型]]
- [[Fama-French数据处理]]
- [[../目录|量化策略总览]]
