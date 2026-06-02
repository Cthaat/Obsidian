---
title: Python金融分析指南
date: 2026-06-02
tags:
  - Python
  - 金融分析
  - 指南
created: 2026-06-02
type: note
source: python-financial-analysis-guide.md
aliases: []
updated: 2026-06-02
---

# Python金融分析指南

> [!note] 本篇定位：收益与风险度量函数库
> 本篇是一套**可直接复用的收益/风险度量函数库**：日收益与对数收益、年化、波动率、夏普 / 索提诺 / 卡玛、回撤曲线。
> 数据怎么向量化、面板怎么对齐见 [[NumPy与Pandas量化指南]] 与 [[量化工具链NumPy与Pandas]]；这些指标如何**画成图**见 [[Python金融分析课程]]。本篇只负责"把数字算对"。

## 一、两种收益率：别混用

```python
import numpy as np
import pandas as pd

TRADING_DAYS = 252   # 年化交易日约定（A股实际约 244-252，按 252 是常见做法）

def simple_returns(prices: pd.Series) -> pd.Series:
    """简单收益率 r_t = P_t / P_{t-1} - 1"""
    return prices.pct_change().dropna()

def log_returns(prices: pd.Series) -> pd.Series:
    """对数收益率 = ln(P_t / P_{t-1})，多期可直接相加"""
    return np.log(prices / prices.shift(1)).dropna()
```

| 类型 | 多期聚合 | 跨资产加权 | 适用场景 |
|------|----------|-----------|----------|
| 简单收益 | 连乘 `(1+r).prod()` | 可直接加权求组合收益 | 组合收益、净值 |
| 对数收益 | 直接求和 | 不可线性加权 | 时序建模、波动估计 |

> [!warning] 第一坑：聚合方式接反
> 对数收益**不能**用 `cumprod`，简单收益**不能**直接相加做多期收益。组合层面用简单收益加权，时序求和用对数收益。

## 二、年化收益与年化波动

```python
def cagr(returns: pd.Series, periods_per_year: int = TRADING_DAYS) -> float:
    """年化复合增长率（几何年化）"""
    growth = (1 + returns).prod()                 # 累计净值倍数
    years = len(returns) / periods_per_year
    return growth ** (1 / years) - 1

def annual_volatility(returns: pd.Series, periods_per_year: int = TRADING_DAYS) -> float:
    """年化波动率：单期波动 × sqrt(期数)"""
    return returns.std(ddof=1) * np.sqrt(periods_per_year)
```

> [!important] 年化因子必须匹配频率
> 日频用 `252`，周频用 `52`，月频用 `12`。波动率按 `sqrt(N)` 缩放（方差与时间成正比），收益按几何方式年化。频率和因子对不上，所有比率都会错。

## 三、三大风险调整收益：夏普 / 索提诺 / 卡玛

$$\text{Sharpe}=\frac{\bar{r}-r_f}{\sigma}\sqrt{N},\quad \text{Sortino}=\frac{\bar{r}-r_f}{\sigma_{down}}\sqrt{N},\quad \text{Calmar}=\frac{\text{年化收益}}{|\text{最大回撤}|}$$

```python
def sharpe_ratio(returns, rf=0.0, periods_per_year=TRADING_DAYS):
    """年化夏普：单位总波动的超额收益"""
    excess = returns - rf / periods_per_year      # 年化无风险利率摊到每期
    sd = excess.std(ddof=1)
    return np.nan if sd == 0 else excess.mean() / sd * np.sqrt(periods_per_year)

def sortino_ratio(returns, rf=0.0, periods_per_year=TRADING_DAYS):
    """索提诺：只惩罚下行波动（上涨不算风险）"""
    excess = returns - rf / periods_per_year
    downside = np.minimum(excess, 0.0)            # 只保留负偏离
    dd = np.sqrt((downside ** 2).mean())          # 目标下行标准差，分母为全部期数
    return np.nan if dd == 0 else excess.mean() / dd * np.sqrt(periods_per_year)

def calmar_ratio(returns, periods_per_year=TRADING_DAYS):
    """卡玛 = 年化收益 / |最大回撤|，衡量"忍受最痛回撤换来的收益" """
    mdd = abs(max_drawdown(returns))
    return np.nan if mdd == 0 else cagr(returns, periods_per_year) / mdd
```

| 比率 | 风险口径 | 何时优先看 |
|------|----------|-----------|
| 夏普 | 总波动（上下都罚） | 通用、可比性强 |
| 索提诺 | 仅下行波动 | 收益分布不对称、怕亏 |
| 卡玛 | 最大回撤 | 关注极端回撤承受力 |

更系统的定义辨析见 [[夏普比率]]。

## 四、回撤曲线与最大回撤

```python
def drawdown_curve(returns: pd.Series) -> pd.Series:
    """回撤曲线：当前净值相对历史峰值的回撤（<=0）"""
    equity = (1 + returns).cumprod()
    peak = equity.cummax()                        # 历史最高净值
    return equity / peak - 1

def max_drawdown(returns: pd.Series) -> float:
    """最大回撤：回撤曲线的最小值"""
    return drawdown_curve(returns).min()
```

> [!tip] 为什么必须用 `cummax`
> 最大回撤是"从历史最高点跌下来的最大幅度"，不是最高价减最低价。`cummax` 维护到当前为止的峰值，才能正确度量"被套最深"的程度。

## 五、一键汇总：组装成绩单

```python
def performance_summary(prices: pd.Series, rf: float = 0.0) -> pd.Series:
    r = simple_returns(prices)
    return pd.Series({
        '年化收益': cagr(r),
        '年化波动': annual_volatility(r),
        '夏普比率': sharpe_ratio(r, rf),
        '索提诺比率': sortino_ratio(r, rf),
        '卡玛比率': calmar_ratio(r),
        '最大回撤': max_drawdown(r),
    })

# ---- 用法（示例数据）----
np.random.seed(1)
idx = pd.date_range('2024-01-01', periods=252, freq='B')
prices = pd.Series(100 * (1 + np.random.normal(0.0005, 0.01, 252)).cumprod(),
                   index=idx, name='close')      # 示例净值序列
print(performance_summary(prices).round(4))
# 示例输出仅供演示，真实数字依输入数据而定
```

这套函数库的输出，正是 [[业绩评估与归因]] 的起点，也是 [[Python金融分析课程]] 画图的输入。

## 六、常见误区 / 踩坑

| 误区 | 后果 | 正确做法 |
|------|------|----------|
| 年化因子张冠李戴 | 所有比率系统性偏差 | 日 252 / 周 52 / 月 12 |
| 对数收益做 `cumprod` | 净值算错 | 对数收益用 `sum`，简单收益用 `prod` |
| 无风险利率不换频率 | 夏普偏大或偏小 | `rf / periods_per_year` 摊到每期 |
| 用总体方差 `ddof=0` | 小样本波动被低估 | 样本统计用 `ddof=1` |
| 最大回撤用 max−min | 高估或低估回撤 | 必须基于 `cummax` |
| 只看夏普 | 忽视胖尾/偏度风险 | 配合索提诺、卡玛、回撤 |
| 不剔除停牌/缺失 | 收益被 0 或 NaN 污染 | 先清洗再 `pct_change`（见姊妹篇） |
| 在样本内调参后报指标 | 过拟合、样本外崩盘 | 留出样本外，参见 [[回测方法论]] |

> [!warning] 夏普不是万能尺
> 夏普假设波动是对称的"风险"，对**左偏/胖尾**收益会高估表现（如卖期权策略平时夏普很高，遇黑天鹅巨亏）。务必与索提诺、最大回撤、卡玛同看。

## 相关链接

- [[Python金融分析课程]]
- [[Python量化入门]]
- [[Python量化金融入门]]
- [[目录|量化策略总览]]
- [[夏普比率]]
- [[业绩评估与归因]]
- [[NumPy与Pandas量化指南]]

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

## 跨领域进阶扩展

> [!tip] 交易者视角
> 学到 `Python金融分析指南` 时，不要只把它当成孤立知识点。把策略视为假设、数据、验证、组合和执行的整体工程。优秀投资交易者会把它放入“宏观背景 - 资产选择 - 估值/信号 - 组合风险 - 交易执行 - 复盘反馈”的闭环。

### 与其他知识的连接

- 收益来源和经济解释
- 数据清洗和偏差控制
- 回测、组合和风控
- 实盘衰减与策略迭代

### 进阶训练

1. 把策略假设写成可证伪命题
2. 建立基准策略比较
3. 把换手、容量和成本纳入绩效评价

### 能力验收

- 能否说清楚这个主题影响的是收益来源、风险来源、交易成本、流动性还是心理纪律？
- 能否指出它在什么市场环境、资产类别或交易周期中更有效？
- 能否把它写成一条可复盘的研究或交易规则？
- 能否说明如果判断错误，组合最大损失和退出机制是什么？

### 全局关联

- [[综合金融知识体系/金融投资全知识地图|金融投资全知识地图]]
- [[综合金融知识体系/优秀投资交易者能力地图|优秀投资交易者能力地图]]
- [[综合金融知识体系/一次性学习路线与复盘模板|一次性学习路线与复盘模板]]
