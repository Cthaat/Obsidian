---
topic: 回测框架
parent: 回测方法
tags: [backtrader, Python, 回测, tutorial]
created: 2026-06-02
---

# Backtrader 实战入门

> [!note] 简介
> Backtrader 是目前Python量化回测领域功能最完善、文档最详细的开源框架。支持多品种、多策略、多周期回测，内置talib指标库，可集成PyTorch/TensorFlow等ML框架。

## 安装

```bash
pip install backtrader
pip install backtrader[plotting]  # 含绘图功能
```

## 核心组件

### 1. 数据加载（Data Feed）

```python
import backtrader as bt
import pandas as pd

# 从pandas DataFrame加载
data = bt.feeds.PandasData(
    dataname=df,
    datetime='date',
    open='open', high='high', low='low',
    close='close', volume='volume',
    openinterest=-1
)
```

### 2. 交易策略（Strategy）

```python
class MyStrategy(bt.Strategy):
    # 可调参数
    params = (
        ('ma_period', 20),
    )

    def __init__(self):
        # 计算指标
        self.sma = bt.indicators.SimpleMovingAverage(
            self.data.close, period=self.params.ma_period
        )

    def next(self):
        # 每个bar执行的逻辑
        if self.data.close[0] > self.sma[0]:
            if not self.position:
                self.buy()  # 买入
        elif self.data.close[0] < self.sma[0]:
            if self.position:
                self.sell()  # 卖出
```

### 3. 回测引擎（Cerebro）

```python
cerebro = bt.Cerebro()
cerebro.adddata(data)           # 添加数据
cerebro.addstrategy(MyStrategy) # 添加策略
cerebro.broker.setcash(100000)  # 初始资金
cerebro.broker.setcommission(commission=0.001)  # 千分之一佣金
cerebro.addsizer(bt.sizers.FixedSize, stake=100)

# 添加分析器
cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')

# 运行回测
results = cerebro.run()

# 绘图
cerebro.plot()
```

### 4. 参数优化

```python
cerebro.optstrategy(
    MyStrategy,
    ma_period=range(10, 31)  # 测试10-30日
)
```

## 常用内置指标

| 指标 | 代码 | 说明 |
|------|------|------|
| 简单移动均线 | `bt.indicators.SMA(period=20)` | SMA |
| 指数移动均线 | `bt.indicators.EMA(period=20)` | EMA |
| MACD | `bt.indicators.MACD()` | 趋势指标 |
| RSI | `bt.indicators.RSI(period=14)` | 超买超卖 |
| 布林带 | `bt.indicators.BollingerBands(period=20)` | 波动率通道 |
| ATR | `bt.indicators.ATR(period=14)` | 平均真实波幅 |

## 实用模式

### Signals 信号模式
更简洁的策略写法，策略直接产生信号：

```python
class SignalStrategy(bt.SignalStrategy):
    def __init__(self):
        sma = bt.ind.SMA(period=20)
        self.signal_add(bt.SIGNAL_LONG, self.data.close > sma)
        self.signal_add(bt.SIGNAL_SHORT, self.data.close < sma)
```

### 多时间框架
```python
class MultiTFStrategy(bt.Strategy):
    def __init__(self):
        # 加载日线和周线
        self.sma_week = bt.ind.SMA(self.datas[1].close, period=10)

    def next(self):
        if self.data.close[0] > self.sma_week[0]:
            self.buy()
```

## 常见问题

- **Lines索引**：`self.data.close[0]` = 当前值，`[-1]` = 前一个
- **佣金**：`cerebro.broker.setcommission(commission=0.001)`
- **滑点**：`cerebro.broker.set_slippage_perc(0.001)`
- **多品种**：多次调用 `cerebro.adddata()`
- **多策略**：多次调用 `cerebro.addstrategy()`

## 进阶扩展
- 集成 **Pyfolio** 做更丰富的绩效分析
- 使用 **Empyrical** 计算 alpha/beta
- 结合 **Alphalens** 做因子分析
- 连接 **IB/Oanda** 等券商实现实盘
