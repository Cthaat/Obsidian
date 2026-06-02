---
title: 配对交易QMT实战
tags:
  - 配对交易
  - QMT
  - 实盘交易
  - 迅投
created: 2026-06-02
type: note
source: pair-trading-cointegration-qmt.md
---

# 配对交易QMT实战

> [!note] QMT实战
> 本文介绍如何在QMT（迅投）平台上实现配对交易策略，从策略编写到实盘执行的完整流程。

## QMT平台简介

QMT是迅投科技开发的量化交易平台，支持：
- Python策略编写
- 实时行情数据
- 自动化交易执行
- 回测和模拟交易

## QMT配对交易实现

### 1. 策略框架
```python
def init(ContextInfo):
    # 初始化
    ContextInfo.stock_a = '600519.SH'  # 贵州茅台
    ContextInfo.stock_b = '000858.SZ'  # 五粮液
    ContextInfo.hedge_ratio = 0.8
    ContextInfo.threshold = 2.0

def handlebar(ContextInfo):
    # 每个bar执行一次
    # 获取数据、计算信号、执行交易
    pass
```

### 2. 信号计算
```python
def calc_signal(ContextInfo):
    # 获取历史数据
    close_a = ContextInfo.get_market_data(['close'], stock_code=ContextInfo.stock_a)
    close_b = ContextInfo.get_market_data(['close'], stock_code=ContextInfo.stock_b)
    
    # 计算价差
    spread = close_a - ContextInfo.hedge_ratio * close_b
    
    # 计算Z-Score
    zscore = (spread - spread.mean()) / spread.std()
    
    return zscore
```

### 3. 交易执行
```python
def execute_trade(ContextInfo, signal):
    if signal < -ContextInfo.threshold:
        # 做多价差：买A卖B
        ContextInfo.order_target_percent(ContextInfo.stock_a, 0.5)
        ContextInfo.order_target_percent(ContextInfo.stock_b, -0.5)
    elif signal > ContextInfo.threshold:
        # 做空价差：卖A买B
        ContextInfo.order_target_percent(ContextInfo.stock_a, -0.5)
        ContextInfo.order_target_percent(ContextInfo.stock_b, 0.5)
```

## 相关链接

- [[配对交易协整理论]]
- [[配对交易Python回测]]
- [[配对交易策略]]
- [[../目录|量化策略总览]]
