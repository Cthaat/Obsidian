---
title: CTA策略Python实战
tags:
  - CTA策略
  - Python
  - 回测
  - 趋势跟踪
created: 2026-06-02
type: note
source: cta-strategy-python-guide.md
---

# CTA策略Python实战

> [!note] Python实现
> 本文介绍如何使用Python实现CTA策略，包括趋势跟踪、截面动量等常见策略的代码实现。

## 趋势跟踪策略实现

### 1. 数据获取
```python
import tushare as ts
import pandas as pd

# 获取期货数据
pro = ts.pro_api()
df = pro.fut_daily(ts_code='CU2301.SHF', start_date='20230101')
```

### 2. 移动平均策略
```python
# 双均线策略
df['SMA_short'] = df['close'].rolling(5).mean()
df['SMA_long'] = df['close'].rolling(20).mean()

# 生成信号
df['signal'] = 0
df.loc[df['SMA_short'] > df['SMA_long'], 'signal'] = 1  # 做多
df.loc[df['SMA_short'] < df['SMA_long'], 'signal'] = -1  # 做空
```

### 3. 唐奇安通道策略
```python
# 唐奇安通道
df['upper'] = df['high'].rolling(20).max()
df['lower'] = df['low'].rolling(20).min()

# 信号
df['signal'] = 0
df.loc[df['close'] > df['upper'].shift(1), 'signal'] = 1
df.loc[df['close'] < df['lower'].shift(1), 'signal'] = -1
```

## 截面动量策略

```python
# 计算多个品种的动量
def calc_momentum(data, window=20):
    return data['close'].pct_change(window)

# 排序选择强势品种
def select_strong(momentum_df, top_n=5):
    return momentum_df.rank(ascending=False) <= top_n
```

## 回测框架

```python
def backtest_cta(data, signal_col, cost=0.0001):
    data['returns'] = data['close'].pct_change()
    data['strategy'] = data[signal_col].shift(1) * data['returns']
    data['strategy_net'] = data['strategy'] - cost * abs(data[signal_col].diff())
    return data
```

## 相关链接

- [[CTA策略详解]]
- [[CTA危机Alpha详解]]
- [[CTA量化论文集]]
- [[../目录|量化策略总览]]
