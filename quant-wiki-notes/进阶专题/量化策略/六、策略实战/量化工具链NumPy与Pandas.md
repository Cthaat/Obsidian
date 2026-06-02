---
title: 量化工具链NumPy与Pandas
tags:
  - NumPy
  - Pandas
  - 工具链
  - 数据处理
created: 2026-06-02
type: note
source: quant-toolchain-numpy-pandas.md
---

# 量化工具链NumPy与Pandas

> [!note] 工具链
> NumPy和Pandas是Python量化投资的核心工具链，分别负责数值计算和数据处理。

## NumPy基础

### 核心功能
- 多维数组操作
- 矩阵运算
- 随机数生成
- 数学函数

### 常用操作
```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])

# 矩阵运算
matrix = np.array([[1, 2], [3, 4]])
inv_matrix = np.linalg.inv(matrix)

# 随机数
random_returns = np.random.normal(0, 0.01, 1000)
```

## Pandas基础

### 核心功能
- DataFrame操作
- 时间序列处理
- 数据清洗
- 分组聚合

### 常用操作
```python
import pandas as pd

# 创建DataFrame
df = pd.DataFrame({
    'close': [100, 101, 102, 103, 104],
    'volume': [1000, 1200, 1100, 1300, 1400]
})

# 计算收益率
df['returns'] = df['close'].pct_change()

# 移动平均
df['SMA'] = df['close'].rolling(3).mean()
```

## 量化应用

| 任务 | NumPy | Pandas |
|-----|-------|--------|
| 收益率计算 | np.diff() | pct_change() |
| 波动率计算 | np.std() | .std() |
| 相关性分析 | np.corrcoef() | .corr() |
| 时间序列 | - | resample() |

## 相关链接

- [[NumPy与Pandas量化指南]]
- [[Python量化入门]]
- [[Python量化进阶]]
- [[../目录|量化策略总览]]
