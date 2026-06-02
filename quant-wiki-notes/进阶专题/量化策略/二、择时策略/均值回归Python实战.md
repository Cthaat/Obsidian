---
title: 均值回归Python实战
tags:
  - 均值回归
  - Python
  - 回测
  - 2025
created: 2026-06-02
type: note
source: mean-reversion-python-guide-2025.md
---

# 均值回归Python实战

> [!note] Python实现
> 本文介绍如何使用Python实现均值回归策略，涵盖数据获取、信号生成、回测验证的完整流程。

## 策略实现步骤

### 1. 数据获取
```python
import yfinance as yf
import pandas as pd

# 获取股票数据
data = yf.download('AAPL', start='2020-01-01', end='2025-01-01')
```

### 2. 计算技术指标
```python
# 布林带
data['SMA'] = data['Close'].rolling(20).mean()
data['Std'] = data['Close'].rolling(20).std()
data['Upper'] = data['SMA'] + 2 * data['Std']
data['Lower'] = data['SMA'] - 2 * data['Std']

# RSI
delta = data['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))
```

### 3. 生成交易信号
```python
# 布林带回归信号
data['Signal'] = 0
data.loc[data['Close'] < data['Lower'], 'Signal'] = 1  # 买入
data.loc[data['Close'] > data['Upper'], 'Signal'] = -1  # 卖出
```

### 4. 回测验证
```python
# 计算策略收益
data['Returns'] = data['Close'].pct_change()
data['Strategy'] = data['Signal'].shift(1) * data['Returns']
```

## 关键参数

| 参数 | 说明 | 典型值 |
|-----|------|-------|
| 回望窗口 | 均值计算周期 | 20日 |
| 标准差倍数 | 布林带宽度 | 2倍 |
| RSI阈值 | 超买超卖水平 | 30/70 |
| 止损线 | 最大亏损限制 | -5% |

## 相关链接

- [[均值回归策略基础]]
- [[均值回归配对交易]]
- [[../目录|量化策略总览]]
