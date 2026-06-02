---
title: Python量化入门
date: 2026-06-02
tags:
  - Python
  - 量化入门
  - 编程
created: 2026-06-02
type: note
source: python-quant-beginner-to-advanced.md, python-quant-step1.md
aliases: []
updated: 2026-06-02
---

# Python量化入门

> [!note] 本篇定位：pandas 数据处理核心
> 环境装好、能拉到数据之后（见 [[Python量化第一步]]），真正占据量化日常 80% 时间的是**数据清洗与整理**。本篇是一本"最常用 pandas 操作手册"——专讲 `DataFrame`、**索引对齐**、`resample`、`rolling`、缺失值处理。
> 这些是把原始行情变成"可用因子"的基本功。把信号变净值、算评估指标，是下一篇 [[Python量化进阶]] 的事；纯数值/矩阵向量化看 [[NumPy与Pandas量化指南]]。

## 一、DataFrame 与 Series：量化数据的容器

- **Series**：带标签的一维数组（如一列收盘价），标签就是**索引**。
- **DataFrame**：多列 Series 拼成的二维表，共享同一行索引。

量化里几乎所有数据都是"**以日期为索引**的 DataFrame"。

```python
import pandas as pd
import numpy as np

# 构造一份示例日线（实际用 akshare 拉取，见《Python量化第一步》）
idx = pd.date_range("2023-01-03", periods=6, freq="B")   # B=工作日
df = pd.DataFrame({
    "close": [10.0, 10.3, 10.1, 10.6, 10.5, 10.9],       # 示例收盘
    "volume": [1.2e6, 1.5e6, 0.9e6, 2.1e6, 1.1e6, 1.8e6],# 示例成交量
}, index=idx)
df.index.name = "date"

print(df.dtypes)          # close/volume 应为 float64
print(df.head())
```

> [!tip] 第一件事：把日期变成 DatetimeIndex
> ```python
> df["date"] = pd.to_datetime(df["date"])
> df = df.set_index("date").sort_index()   # 排序后切片/重采样才正确
> ```
> 只有真正的 `DatetimeIndex` 才能用 `df.loc["2023-06"]` 这种按时间切片，以及后面的 `resample`。

## 二、选取与按时间切片

| 写法 | 含义 |
|------|------|
| `df["close"]` | 取一列（Series） |
| `df`"close", "volume"`` | 取多列（DataFrame） |
| `df.loc["2023-06"]` | 取 2023 年 6 月所有行（标签切片） |
| `df.loc["2023-06":"2023-08"]` | 时间区间，**含右端** |
| `df.iloc[0]` / `df.iloc[-1]` | 按位置取第一/最后一行 |
| `df[df["volume"] > 1e6]` | 布尔过滤 |

> [!warning] `loc`（标签）与 `iloc`（位置）别混用
> `df.loc[0]` 在 `DatetimeIndex` 下会报错（没有标签 0）；想按位置取第一行用 `df.iloc[0]`。**标签切片 `loc` 含右端，位置切片 `iloc` 不含右端**，这是高频混淆点。

## 三、索引对齐：pandas 最强也最易踩的特性

pandas 做算术时会**按索引自动对齐**，对不上的位置填 `NaN`。这既是利器，也是 bug 之源。

```python
a = pd.Series([1, 2, 3], index=["2023-01-03", "2023-01-04", "2023-01-05"])
b = pd.Series([10, 20, 30], index=["2023-01-04", "2023-01-05", "2023-01-06"])

print(a + b)
# 2023-01-03    NaN   <- a 有 b 无
# 2023-01-04   12.0
# 2023-01-05   23.0
# 2023-01-06    NaN   <- b 有 a 无
```

> [!important] 对齐 = 自动防错，但也会"偷偷"产生 NaN
> 两只股票交易日不完全相同（停牌、上市时间差）时，直接相减得到的价差会在缺失日变 `NaN`。**这其实是好事**——它阻止你把"不同日期"的数据错位相减。需要严格同日数据时，先 `join`/`align` 取交集：
> ```python
> aligned = pd.concat([a, b], axis=1, join="inner")  # 只保留共同日期
> ```

## 四、rolling：滚动窗口（均线、滚动波动率）

`rolling(window)` 在时间序列上开一个定长窗口逐步滑动，是均线、滚动标准差的标准工具。

```python
df["ma3"] = df["close"].rolling(window=3).mean()          # 3日均线
df["std3"] = df["close"].rolling(window=3).std()          # 3日滚动标准差
df["max3"] = df["close"].rolling(window=3).max()          # 3日最高（唐奇安通道用）

# 前 window-1 行因数据不足为 NaN，这是正常且必要的
print(df`"close", "ma3", "std3"`)
```

> [!warning] rolling 默认"右对齐"——窗口看的是"过去"
> `rolling(3)` 在第 t 行用的是 `[t-2, t-1, t]`，**包含当前行**。这通常没问题（当日收盘已知）。但若你用"含当日均线"去生成"当日就交易"的信号，再乘"当日收益"，就引入了未来函数。规避方式是把信号 `shift(1)` 后再用——详见 [[Python量化进阶]]。

| 需求 | 写法 |
|------|------|
| N 日均线 | `s.rolling(N).mean()` |
| N 日波动率 | `s.rolling(N).std()` |
| 至少 k 个值才算 | `s.rolling(N, min_periods=k)` |
| 指数加权均线 | `s.ewm(span=N).mean()` |
| 扩张窗口（累计） | `s.expanding().max()` |

## 五、resample：改变时间频率（日 → 周/月）

把日线聚合成周线/月线，或把高频降采样，用 `resample`。它要求索引是 `DatetimeIndex`。

```python
# 日线 -> 周线：开高低收用不同聚合方式
weekly = df["close"].resample("W").last()        # 周收盘 = 当周最后一个值
weekly_vol = df["volume"].resample("W").sum()    # 周成交量 = 求和

# 一次性聚合多列（OHLC 风格）
agg = df.resample("M").agg({
    "close": "last",      # 月末收盘
    "volume": "sum",      # 月成交量合计
})
print(agg)
```

> [!tip] resample vs rolling 别搞混
> - `rolling`：**频率不变**，每行都有一个滑动窗口结果（行数不变）。
> - `resample`：**频率改变**，把多行压缩成一行（行数减少）。
> 算"20 日均线"用 rolling；把"日线变月线"用 resample。

## 六、缺失值（NaN）处理

停牌、节假日、对齐都会产生 `NaN`。处理策略要**贴合金融语义**。

```python
df2 = df.copy()
df2.loc["2023-01-05", "close"] = np.nan          # 制造一个缺失（示例）

print(df2["close"].isna().sum())                 # 数一下缺几个

# 价格类：通常用"前值填充"（停牌期间价格视为不变）
df2["close_ffill"] = df2["close"].ffill()

# 收益率类：缺失日往往应视为 0 收益，或直接剔除
ret = df2["close_ffill"].pct_change()
ret = ret.fillna(0)                              # 视情况：填0 或 dropna()
```

| 场景 | 推荐处理 | 理由 |
|------|---------|------|
| 价格停牌缺失 | `ffill()` 前值填充 | 停牌期价格不变 |
| 收益率首行 NaN | `fillna(0)` 或 `dropna()` | 第一天无前值 |
| 指标预热期 NaN | 保留，不强行填 | 数据不足本就不该有信号 |
| 大段连续缺失 | 谨慎，考虑剔除该标的 | 填充会造假 |

> [!warning] 不要无脑 `fillna(0)` 价格
> 把缺失**价格**填 0 会制造一根"暴跌到 0 再暴涨"的假 K 线，收益率瞬间爆表。价格缺失用 `ffill`，把"填 0"留给**收益率/信号**这类语义上为 0 合理的列。

## 七、把它们串起来：一段典型的数据准备

```python
def prepare(df_raw: pd.DataFrame) -> pd.DataFrame:
    """从原始行情到'可用于建因子'的干净数据（示例流程）"""
    df = df_raw.copy()                                  # 不就地改原始数据
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date").sort_index()              # 时间索引 + 升序
    df["close"] = df["close"].ffill()                   # 价格前值填充
    df["ret"] = df["close"].pct_change()                # 日收益
    df["ma20"] = df["close"].rolling(20).mean()         # 20日均线
    df["vol20"] = df["ret"].rolling(20).std()           # 20日波动率
    return df.dropna(subset=["ma20"])                   # 去掉预热期不足的行
```

```mermaid
graph LR
    A[原始行情] --> B[转 datetime + 排序]
    B --> C[价格 ffill]
    C --> D[算收益 / 均线 / 波动率]
    D --> E[dropna 去预热期] --> F[干净数据]
```

## 八、常见误区 / 踩坑

| 误区 | 后果 | 正确做法 |
|------|------|----------|
| 不转 `DatetimeIndex` | 无法时间切片/resample | `pd.to_datetime` + `set_index` |
| 忘了 `sort_index` | `pct_change`/`diff` 算反方向 | 取数后立即排序 |
| `loc` 与 `iloc` 混用 | KeyError 或取错行 | 标签用 `loc`，位置用 `iloc` |
| 忽视索引自动对齐 | 跨标的相减"凭空" NaN | 先 `align/concat join='inner'` |
| 链式赋值 `df[m]['col']=x` | `SettingWithCopyWarning`，没改成功 | 用 `df.loc[mask, 'col']=x` |
| 就地修改传入的 df | 污染调用方原始数据 | 函数内先 `.copy()` |
| `fillna(0)` 填价格 | 制造假暴跌 | 价格用 `ffill` |
| 用含当日的 rolling 做当日信号 | 未来函数 | 信号 `shift(1)`（见进阶篇） |

> [!warning] SettingWithCopyWarning 的根因
> ```python
> df[df["close"] > 10]["close"] = 99   # ❌ 在切片副本上改，原表没变
> df.loc[df["close"] > 10, "close"] = 99  # ✅ 一次定位行+列
> ```
> 第一种写法 pandas 不保证改的是原表还是副本，所以警告。**永远用单次 `.loc[行, 列]` 赋值。**

## 相关链接

- [[Python量化进阶]]
- [[Python量化3小时精通]]
- [[量化工具链NumPy与Pandas]]
- [[目录|量化策略总览]]
- [[Python量化第一步]]
- [[NumPy与Pandas量化指南]]
- [[Python量化金融入门]]

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
