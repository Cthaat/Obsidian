---
title: 配对交易Python回测
tags:
  - 配对交易
  - Python
  - 回测
  - 协整
created: 2026-06-02
type: note
source: pair-trading-python-backtest.md
---

# 配对交易Python回测

> [!note] Python回测
> 本文介绍如何使用Python实现配对交易策略的完整回测流程。

## 完整回测代码

### 1. 数据准备
```python
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import coint

# 获取两只股票数据
stock_a = pd.read_csv('stock_a.csv')['close']
stock_b = pd.read_csv('stock_b.csv')['close']
```

### 2. 协整检验
```python
# 协整检验
score, pvalue, _ = coint(stock_a, stock_b)
print(f'协整检验p值: {pvalue:.4f}')

if pvalue < 0.05:
    print('存在协整关系，可以进行配对交易')
```

### 3. 计算对冲比例和价差
```python
import statsmodels.api as sm

# OLS回归确定对冲比例
X = sm.add_constant(stock_b)
model = sm.OLS(stock_a, X).fit()
hedge_ratio = model.params[1]
intercept = model.params[0]

# 计算价差
spread = stock_a - hedge_ratio * stock_b - intercept
```

### 4. 生成交易信号
```python
# Z-Score标准化
zscore = (spread - spread.mean()) / spread.std()

# 交易信号
longs = zscore < -2    # 做多价差（买A卖B）
shorts = zscore > 2    # 做空价差（卖A买B）
exits = abs(zscore) < 0.5  # 平仓
```

### 5. 回测计算
```python
# 计算策略收益
position = pd.Series(0, index=spread.index)
position[longs] = 1
position[shorts] = -1
position[exits] = 0
position = position.ffill()

returns_a = stock_a.pct_change()
returns_b = stock_b.pct_change()
strategy_returns = position * (returns_a - hedge_ratio * returns_b)
```

## 回测指标

| 指标 | 说明 | 计算方法 |
|-----|------|---------|
| 年化收益 | 策略年化回报 | 总收益/年数 |
| 最大回撤 | 最大亏损幅度 | 净值峰谷差 |
| 夏普比率 | 风险调整收益 | 收益/波动率 |
| 胜率 | 盈利交易占比 | 盈利次数/总次数 |

## 相关链接

- [[配对交易协整理论]]
- [[配对交易QMT实战]]
- [[配对交易策略]]
- [[../目录|量化策略总览]]
