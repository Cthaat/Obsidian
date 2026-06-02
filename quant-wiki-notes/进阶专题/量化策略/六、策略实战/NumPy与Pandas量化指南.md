---
title: NumPy与Pandas量化指南
tags:
  - NumPy
  - Pandas
  - 量化指南
created: 2026-06-02
type: note
source: python-numpy-pandas-quant-guide.md
---

# NumPy与Pandas量化指南

> [!note] 量化指南
> NumPy和Pandas在量化投资中的详细应用指南，涵盖数据处理、分析和建模。

## 数据处理流程

### 1. 数据读取
```python
import pandas as pd

# 读取CSV数据
data = pd.read_csv('stock_data.csv', parse_dates=['date'], index_col='date')

# 读取Excel数据
data = pd.read_excel('stock_data.xlsx')
```

### 2. 数据清洗
```python
# 处理缺失值
data = data.dropna()  # 删除缺失值
data = data.fillna(method='ffill')  # 前向填充

# 处理异常值
data = data[data['close'] > 0]  # 删除负值
```

### 3. 数据转换
```python
# 计算收益率
data['returns'] = data['close'].pct_change()

# 计算对数收益率
data['log_returns'] = np.log(data['close'] / data['close'].shift(1))

# 计算累计收益
data['cum_returns'] = (1 + data['returns']).cumprod()
```

## 常用统计函数

```python
# 描述统计
data['returns'].describe()

# 相关性矩阵
data[['stock_a', 'stock_b', 'stock_c']].corr()

# 滚动统计
data['returns'].rolling(20).mean()  # 滚动均值
data['returns'].rolling(20).std()   # 滚动标准差
```

## 相关链接

- [[量化工具链NumPy与Pandas]]
- [[Python量化入门]]
- [[Python金融分析课程]]
- [[../目录|量化策略总览]]
