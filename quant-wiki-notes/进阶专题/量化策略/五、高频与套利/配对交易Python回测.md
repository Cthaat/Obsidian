---
title: 配对交易Python回测
date: 2026-06-02
tags:
  - 配对交易
  - Python
  - 回测
  - 协整
created: 2026-06-02
type: note
source: pair-trading-python-backtest.md
aliases: []
updated: 2026-06-02
---

# 配对交易Python回测

> [!note] Python回测
> 本文给出配对交易**可运行的回测骨架**：从取数、协整检验、构建价差、滚动 Z-Score、开平仓信号，到收益与绩效评估，逐段拆解并标注实战要点。复制即可在本地跑通（数据自备）。

## 一、回测全流程总览

```mermaid
flowchart LR
    A[取数据 close_a/close_b] --> B[协整检验 coint]
    B --> C[OLS 估 β 与截距]
    C --> D[构建价差 spread]
    D --> E[滚动 Z-Score]
    E --> F[生成持仓 position]
    F --> G[shift1 防未来函数]
    G --> H[策略收益]
    H --> I[绩效: 年化/回撤/夏普]
```

## 二、数据准备

```python
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import coint, adfuller
import statsmodels.api as sm

# 读入两只股票收盘价（索引为日期，按日期对齐）
stock_a = pd.read_csv('stock_a.csv', index_col=0, parse_dates=True)['close']
stock_b = pd.read_csv('stock_b.csv', index_col=0, parse_dates=True)['close']

# 关键：按日期内连接对齐，去除缺失，防止错位
df = pd.concat([stock_a, stock_b], axis=1, keys=['A', 'B']).dropna()
stock_a, stock_b = df['A'], df['B']
```

> [!warning] 对齐与复权
> 两只股票必须**按交易日严格对齐**（停牌日要剔除或对齐），否则价差全错。价格务必用**前复权**序列，否则除权除息会造成价差假突变。

## 三、协整检验

```python
score, pvalue, _ = coint(stock_a, stock_b)
print(f'协整检验 p 值: {pvalue:.4f}')
assert pvalue < 0.05, '不协整，不应进行配对交易'
```

> [!important] 协整应在样本内做
> 协整检验和 β 估计应只用**训练样本**（in-sample），再到**样本外**（out-of-sample）回测。用全样本检验再全样本回测，是自欺欺人。详见 [[配对交易协整理论]]。

## 四、估计对冲比率与价差

```python
# OLS：A = α + β·B + ε，β 即对冲比率
X = sm.add_constant(stock_b)
model = sm.OLS(stock_a, X).fit()
intercept, hedge_ratio = model.params.iloc[0], model.params.iloc[1]

# 价差（残差）
spread = stock_a - hedge_ratio * stock_b - intercept

# 价差应平稳
adf_p = adfuller(spread.dropna())[1]
print(f'价差 ADF p 值: {adf_p:.4f}')
```

## 五、滚动 Z-Score（核心红线）

```python
WINDOW = 60  # 滚动窗口（示例：60 个交易日）

roll_mean = spread.rolling(WINDOW).mean()
roll_std  = spread.rolling(WINDOW).std()
zscore = (spread - roll_mean) / roll_std
```

> [!warning] 绝不要用全样本均值方差
> ```python
> # 错误示范（引入未来信息，回测虚高）：
> # zscore = (spread - spread.mean()) / spread.std()
> ```
> 全样本 `mean()/std()` 让每一天都"知道"了整个历史，回测漂亮、实盘必亏。**务必用 `rolling`。** 这是配对交易回测最常见、最致命的错误。

## 六、生成交易信号与持仓

```python
ENTRY, EXIT, STOP = 2.0, 0.5, 3.5  # 开仓/平仓/止损阈值（示例）

position = pd.Series(np.nan, index=zscore.index)
position[zscore < -ENTRY] = 1     # 做多价差：买A卖B
position[zscore >  ENTRY] = -1    # 做空价差：卖A买B
position[zscore.abs() < EXIT] = 0 # 回归平仓
position[zscore.abs() > STOP] = 0 # 止损平仓
position = position.ffill().fillna(0)
```

> [!tip] 信号要"先有持仓，再吃收益"
> 用 `ffill` 让持仓在开仓后保持，直到遇到平仓/止损/反向信号。`np.nan` 初始化 + `ffill` 是优雅表达"维持上一状态"的常用写法。

## 七、防未来函数 + 计算策略收益

```python
# 关键：用今天收盘的信号，赚明天的收益 → 持仓滞后一日
pos = position.shift(1).fillna(0)

ret_a = stock_a.pct_change()
ret_b = stock_b.pct_change()

# 价差组合收益（做多价差 = +A -β·B）
gross = pos * (ret_a - hedge_ratio * ret_b)

# 扣成本：换手时按双边费率计（示例 0.1%/边）
FEE = 0.001
turnover = pos.diff().abs().fillna(0)
cost = turnover * FEE
net = gross - cost

equity = (1 + net).cumprod()  # 净值曲线
```

> [!warning] 两个最常见的回测谎言
> 1. **未来函数**：不 `shift(1)` 就用当日信号当日收益，等于"看着今天收盘价决定今天开盘买"——实盘做不到。
> 2. **零成本**：不扣手续费、印花税、冲击、做空成本。配对交易换手高，成本能吃掉大半理论收益。

## 八、绩效评估

```python
def performance(net_returns, equity, periods_per_year=252):
    cum = equity.iloc[-1] - 1
    years = len(net_returns) / periods_per_year
    cagr = (equity.iloc[-1]) ** (1 / years) - 1
    sharpe = np.sqrt(periods_per_year) * net_returns.mean() / (net_returns.std() + 1e-9)
    drawdown = (equity / equity.cummax() - 1).min()
    return dict(累计收益=cum, 年化=cagr, 夏普=sharpe, 最大回撤=drawdown)

print(performance(net, equity))
```

| 指标 | 含义 | 计算要点 |
|------|------|---------|
| 年化收益 CAGR | 复合年化回报 | 由净值与年数推 |
| 最大回撤 | 净值峰谷最大跌幅 | `equity/equity.cummax()-1` 的最小值 |
| 夏普比率 | 单位波动的超额收益 | 年化时乘 $\sqrt{252}$ |
| 胜率 | 盈利交易占比 | 按"每次平仓"统计，非按日 |

> [!note] 夏普不是唯一
> 配对交易还要看：换手率（成本敏感度）、单笔平均持仓天数（是否匹配半衰期）、最长不回归时间、收益是否集中在少数几笔（脆弱）。

## 九、提升回测严谨度（进阶清单）

> [!example] 把"玩具回测"升级为"可信回测"
> - **样本外验证**：训练集估 β/阈值，测试集才计收益。
> - **滚动再估计**：定期重做协整与 β，模拟真实运维。
> - **多配对组合**：跑一篮子配对看组合稳健性，别只信一对。
> - **成本敏感性**：把费率从 0.05% 调到 0.3%，看策略是否还活着。
> - **参数稳健性**：窗口、阈值小幅扰动，绩效应平滑变化而非剧变（剧变=过拟合）。
> - **A 股做空约束**：标记空头腿是否有融券可用，否则收益不可实现。

完整方法学见 [[回测方法论]]；落到实盘的工程要点见 [[配对交易QMT实战]]。

## 十、常见误区与风险

> [!warning] 回测六大坑
> 1. **全样本 Z-Score**（最致命）→ 用 `rolling`。
> 2. **未来函数**：不 `shift(1)`。
> 3. **零成本幻觉**：不扣手续费/印花税/做空成本。
> 4. **幸存者偏差**：只测当下还活着的好配对。
> 5. **过拟合阈值/窗口**：在历史上调到完美。
> 6. **忽视停牌/涨跌停**：信号日无法成交却照算收益。

> [!important] 回测漂亮 ≠ 能赚钱
> 配对交易的回测尤其容易"骗自己"——价差均值回归本身就让历史曲线很顺。真正的检验是**严格样本外 + 真实成本 + 可执行性约束**三者同时通过。任何一项放水，结论都不可信。

## 相关链接

- [[配对交易协整理论]]
- [[配对交易QMT实战]]
- [[配对交易策略]]
- [[统计套利深度解析]]
- [[回测方法论]]
- [[目录|量化策略总览]]

## 课程化学习补充

> [!important] 学习定位
> 量化策略是投资假设、数据工程、回测验证、风险预算和执行系统的组合，不是单一公式。本文仅用于学习、研究与复盘，不构成任何投资建议。

### 必须掌握的问题

- 假设是否可证伪
- 数据是否 point-in-time
- 绩效是否扣除真实成本
- 上线后是否监控衰减

### 实战应用流程

1. 先写清楚你的投资假设：为什么这个信号、资产或方法应该产生收益。
2. 明确数据口径：样本范围、更新时间、复权/分红/停牌处理和交易日历。
3. 做最小可行验证：先用简单规则验证方向，再逐步加入复杂模型。
4. 把成本和约束前置：手续费、滑点、冲击成本、保证金、流动性和容量都要进入测算。
5. 上线后持续复盘：记录信号、下单、成交、持仓、回撤和失效原因。

### 风险与失效条件

- 数据挖掘偏差
- 因子拥挤
- 换手过高
- 实盘偏离回测

### 复盘问题

- 这笔交易或这套模型赚的是什么钱：风险补偿、行为偏差、流动性溢价，还是偶然噪音？
- 如果市场环境反过来，最大亏损和最长恢复期会是多少？
- 当前结论是否依赖某个不可持续假设，例如低利率、低波动、充裕流动性或监管套利？
- 有没有一个更简单的基准策略能取得接近效果？

### 延伸学习

- [[量化投资完全指南]]
- [[回测质量门清单]]
- [[市场微观结构与交易执行]]
- [[量化风险管理体系]]
