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
