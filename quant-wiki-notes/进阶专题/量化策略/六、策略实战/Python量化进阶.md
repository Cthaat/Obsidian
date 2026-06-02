---
title: Python量化进阶
date: 2026-06-02
tags:
  - Python
  - 量化进阶
  - 回测引擎
  - 高级技巧
created: 2026-06-02
type: note
source: python-quant-tutorial-runoo.md
aliases: []
updated: 2026-06-02
---

# Python量化进阶

> [!note] 本篇定位
> [[Python量化入门]] 教你用 pandas 处理数据，这一篇带你**自己动手写一个最小但正确的向量化回测引擎**——从信号到净值到评估指标。理解回测的每一步，才不会被现成框架的黑箱坑到。重点不是写得多花哨，而是把"未来函数、成本、过拟合"这三件最容易出错的事做对。

## 一、回测引擎的最小骨架

任何回测，本质都是同一条流水线：

```mermaid
graph LR
    A[价格数据] --> B[生成信号 signal]
    B --> C[转成持仓 position]
    C --> D[计算策略收益 strategy_ret]
    D --> E[累计净值 equity]
    E --> F[评估指标]
```

关键只有一句话：**今天的持仓只能用今天收盘前已知的信息决定，明天才产生收益**。这句话用代码表达就是一个 `shift(1)`，也是新手最常犯错的地方。

## 二、向量化实现：不用 for 循环

以"双均线"策略为例（短均线上穿长均线做多，下穿空仓）。下面全部用向量化，几行就能跑完几十年数据。

```python
import numpy as np
import pandas as pd

def backtest(price: pd.Series, short=20, long=60, cost=0.0005) -> pd.DataFrame:
    df = pd.DataFrame({"price": price})
    df["ret"] = df["price"].pct_change()           # 当日收益

    # 1) 信号：短均线 > 长均线 → 想持有
    ma_s = df["price"].rolling(short).mean()
    ma_l = df["price"].rolling(long).mean()
    df["signal"] = (ma_s > ma_l).astype(int)

    # 2) 持仓：关键！用 shift(1) 把信号推迟一天，避免未来函数
    df["position"] = df["signal"].shift(1).fillna(0)

    # 3) 交易成本：持仓变化时才扣费
    df["trade"] = df["position"].diff().abs().fillna(0)
    df["cost"] = df["trade"] * cost

    # 4) 策略收益与净值
    df["strat_ret"] = df["position"] * df["ret"] - df["cost"]
    df["equity"] = (1 + df["strat_ret"]).cumprod()
    df["bench"] = (1 + df["ret"]).cumprod()
    return df
```

> [!warning] 未来函数（look-ahead bias）
> 如果写成 `df["position"] = df["signal"]`（不 `shift`），相当于"用今天收盘后才知道的信号，去赚今天的收益"。回测会好看得离谱，实盘必然崩。**80% 的"圣杯策略"都死在这一行。**

## 三、加入更真实的成本

真实成本不止佣金，还有滑点、冲击、印花税。可以拆开建模：

```python
def apply_costs(position: pd.Series, ret: pd.Series,
                commission=0.0003, slippage=0.0010, stamp=0.0005):
    trade = position.diff().abs().fillna(0)
    # 卖出才收印花税（A股），这里简化为换手都计一半
    cost = trade * (commission + slippage) + (trade * stamp * 0.5)
    return position * ret - cost
```

| 成本类型 | 量级（示例，A股） | 说明 |
|---|---|---|
| 佣金 | 万分之 1.5~3 | 双边收取 |
| 印花税 | 千分之 0.5~1 | 卖出单边 |
| 滑点 | 千分之 0.5~2 | 与流动性、下单方式相关 |
| 冲击成本 | 随单量上升 | 大单尤其明显 |

> [!tip] 经验法则
> 高换手策略对成本极其敏感。一个回测年化 30% 的日频策略，把双边成本从 0 提到千分之 2，年化可能直接腰斩。**先加成本，再谈收益。**

## 四、评估指标

```python
def metrics(strat_ret: pd.Series, freq=252) -> dict:
    equity = (1 + strat_ret).cumprod()
    ann_ret = equity.iloc[-1] ** (freq / len(strat_ret)) - 1
    ann_vol = strat_ret.std() * np.sqrt(freq)
    sharpe = ann_ret / ann_vol if ann_vol > 0 else np.nan
    drawdown = equity / equity.cummax() - 1
    return {
        "年化收益": round(ann_ret, 4),
        "年化波动": round(ann_vol, 4),
        "夏普": round(sharpe, 2),
        "最大回撤": round(drawdown.min(), 4),
        "卡玛": round(ann_ret / abs(drawdown.min()), 2) if drawdown.min() < 0 else np.nan,
    }
```

| 指标 | 含义 | 看什么 |
|---|---|---|
| 年化收益 | 几何年化 | 别只看这一个 |
| 年化波动 | 收益标准差年化 | 颠簸程度 |
| 夏普比率 | 单位波动的超额收益 | 风险调整后好不好 |
| 最大回撤 | 净值峰谷最大跌幅 | 你扛不扛得住 |
| 卡玛比率 | 年化收益 / 最大回撤 | 痛苦换收益的性价比 |

指标的详细解读见 [[业绩评估与归因]]。

## 五、参数优化与过拟合

网格搜索很容易写，但**这正是危险所在**：

```python
from itertools import product

def grid_search(price, shorts=range(5, 30, 5), longs=range(30, 120, 10)):
    rows = []
    for s, l in product(shorts, longs):
        if s >= l:
            continue
        df = backtest(price, s, l)
        m = metrics(df["strat_ret"].dropna())
        rows.append({"short": s, "long": l, **m})
    return pd.DataFrame(rows).sort_values("夏普", ascending=False)
```

> [!important] 最好看的参数，往往是最过拟合的
> 在同一段历史上挑出夏普最高的参数，本质是"在噪声里找规律"。正确做法：
> - **样本外测试**：留出最后 1/3 数据完全不参与调参；
> - **走向前分析（walk-forward）**：滚动地"用过去调参、在未来验证"；
> - **看参数高原而非尖峰**：相邻参数表现都不错（高原）才稳健，孤零零一个尖峰多半是运气。
>
> 更系统的回测陷阱见 [[回测方法论]]。

## 六、从单资产到多资产

多品种时，把价格组织成"日期 × 标的"的宽表，仍可向量化：

```python
# prices: index=日期, columns=标的代码
rets = prices.pct_change()
signals = (prices > prices.rolling(60).mean()).astype(int)
positions = signals.shift(1).div(signals.shift(1).sum(axis=1), axis=0)  # 等权分配
port_ret = (positions * rets).sum(axis=1)
```

截面策略（同时在多只标的上多空）的权重与风险分配，见 [[组合构建方法]] 与 [[风险管理框架]]。

## 七、常见误区与踩坑

| 误区 / 坑 | 后果 | 正确做法 |
|---|---|---|
| 信号不 `shift(1)` | 未来函数，回测虚高 | 持仓用上一期信号 |
| 忽略交易成本 | 高换手策略实盘亏损 | 先建模成本再评估 |
| 在全样本上调参 | 过拟合，样本外失效 | 样本外 + 走向前 |
| 用 `inplace=True` 改原数据 | 后续计算污染、难复现 | 返回新对象，链式调用 |
| 幸存者偏差的股票池 | 高估收益 | 用含退市的历史成分 |
| 只看年化、不看回撤 | 实盘拿不住 | 夏普、回撤、卡玛一起看 |

> [!tip] 进阶方向
> 写顺了最小引擎后，可以学成熟框架（如 backtrader、vectorbt、zipline），但**原理永远是这套流水线**。框架解决的是事件驱动、撮合细节、多周期对齐，不是替你免掉对未来函数和成本的思考。

## 相关链接

- [[Python量化入门]]
- [[Python量化3小时精通]]
- [[量化工具链NumPy与Pandas]]
- [[回测方法论]]
- [[业绩评估与归因]]
- [[目录|量化策略总览]]

## 实战掌握清单

> [!tip] 交易者视角
> Python量化进阶 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化策略必须从清晰假设出发，经过数据验证、成本测算、风险控制和实盘监控，才可能成为可持续系统。

### 关键判断

- 写清楚收益来自动量、反转、价值、套利、波动率、流动性还是行为偏差。
- 确认信号、过滤器、入场、退出、仓位和风控。
- 看收益是否集中在少数时期、少数品种或少数参数。

### 落地动作

1. 做样本外、滚动窗口和参数扰动测试。
2. 把手续费、滑点、冲击成本、容量和失败交易纳入报告。
3. 上线后监控成交质量、信号衰减、回撤和异常订单。

### 失效边界

- 过拟合。
- 策略容量不足。
- 市场结构变化后没有停止机制。

### 复盘问题

- 这项知识改变了哪一个具体决策：标的、方向、仓位、退出、对冲还是不交易？
- 如果判断相反，最大亏损、最长恢复期和退出触发条件是什么？
- 有没有一个更简单的基准方法可以取得相近结果？
