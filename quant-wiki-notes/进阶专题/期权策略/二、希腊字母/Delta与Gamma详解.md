---
title: Delta与Gamma详解
tags:
  - Delta
  - Gamma
  - 希腊字母
  - 对冲
created: 2026-06-02
source: 整合自多个来源
---

# Delta与Gamma详解

> [!note] 核心要点
> Delta 衡量方向性风险，是期权价格对标的价格的一阶导数；Gamma 衡量 Delta 的变化速率，是二阶导数。两者共同构成期权的方向性风险管理体系。

---

## 一、Delta 深度解析

### 1.1 数学定义

$$\Delta_{\text{call}} = \frac{\partial C}{\partial S} = N(d_1)$$

$$\Delta_{\text{put}} = \frac{\partial P}{\partial S} = N(d_1) - 1$$

### 1.2 三层含义

**第一层：价格敏感度**
Call Delta 0.5 意味着标的涨 \$1，期权价格大约涨 \$0.50。说"大约"是因为这是线性近似，Delta 本身也在变（这就是 Gamma 的事）。

**第二层：对冲比率**
持有 1 手 Delta 0.5 的 Call（合约乘数 100），需要卖空 50 股标的才能构建 Delta 中性头寸。做市商每天做的事情本质上就是这个：不断调整标的持仓，让组合的净 Delta 接近零。

$$\Delta = 0.6 \Rightarrow \text{持有 1 份期权需卖空 } 0.6 \text{ 单位股票}$$

**第三层：近似到期概率**
Delta 的绝对值可以粗略理解为期权到期时处于实值状态的概率。
- Delta 0.3 的 Call ≈ 30% 概率到期实值
- 精确值是 $N(d_2)$ 而不是 $N(d_1)$，但快速评估时够用

### 1.3 Delta 的特性

| 特性 | 说明 |
|------|------|
| Call 取值范围 | [0, 1] |
| Put 取值范围 | [-1, 0] |
| ATM 期权 | Delta ≈ 0.5（Call）或 -0.5（Put） |
| 深度实值 | Delta → 1（Call）或 -1（Put） |
| 深度虚值 | Delta → 0 |

> [!tip] Delta 与行权价的关系
> - 行权价越高，Call 的 Delta 越低
> - 深度虚值期权：股价变动几乎不影响期权价格，Delta ≈ 0
> - 深度实值期权：持有期权类似持有正股，Delta ≈ 1

### 1.4 Delta 的高阶应用

**组合 Delta 可加性**：期权组合中每个子期权的 Delta 可以加减运算，得出组合整体的方向性敞口。

$$\Delta_{\text{组合}} = \sum_{i} \Delta_i$$

**Delta 对冲频率**：理论上 BSM 假设连续对冲，但现实中需要在交易成本和 Gamma 暴露之间权衡。做市商通常设一个 Delta 带宽：净 Delta 超过阈值才触发对冲。

### 1.5 Delta 与隐含波动率/时间的关系

- **IV 上升** → Delta 趋向 0.50（更多行权价进入波动范围）
- **临近到期** → ITM 的 Delta → 1，OTM 的 Delta → 0，ATM 的 Delta ≈ 0.5

---

## 二、Gamma 深度解析

### 2.1 数学定义

$$\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{N'(d_1)}{S \cdot \sigma \cdot \sqrt{T}}$$

Gamma 的值恒为正（Call 和 Put 一样）。

### 2.2 核心特性

| 特性 | 说明 |
|------|------|
| 最大值位置 | ATM 附近 |
| 时间影响 | 临到期时 Gamma 急剧增大 |
| 买方/卖方 | 买方为正，卖方为负 |

### 2.3 Long Gamma vs Short Gamma

**Long Gamma（买期权）**：
- 标的怎么动都不吃亏：涨了多赚，跌了少亏
- 代价：每天被 Theta 吃掉一点时间价值
- 四字总结：**涨多跌少**

**Short Gamma（卖期权）**：
- 每天白捡 Theta
- 风险：标的大幅跳空时，Gamma 把之前赚的 Theta 全部吐回去
- 四字总结：**跌多涨少**

> [!example] Long Gamma 数字示例
> 假设持有 ATM Call，Gamma = 0.03，Delta = 0.50。标的从 100 涨到 105：
> - Delta 变成约 0.65（= 0.50 + 0.03 × 5）
> - 赚的不是 $0.50 \times 5 = 2.50$，而是约 $(0.50 + 0.65)/2 \times 5 = 2.875$
> - 多出来的 0.375 就是 Gamma 带来的"**凸性收益**"
> 
> 反过来标的跌 5 块，亏的是约 $(0.50 + 0.35)/2 \times 5 = 2.125$，比线性估计的 2.50 少亏 0.375。

### 2.4 Gamma Risk

从两个维度理解：

**股价维度**：ATM 的 Gamma 最大，因为 ATM 是期权能否赚钱的临界点，期权价格对股价变动尤为敏感。

**时间维度**：越是临近到期的期权，Gamma 越大。末日轮期权高波动的原因就是不可控的 Gamma。

> [!warning] 临到期 Gamma 风险
> 临到期的 ATM 期权，标的稍微动一下 Delta 就剧烈变化，对冲难度极大。这就是做市商在到期日前一两天特别紧张的原因——所谓的 **Gamma Risk**。

### 2.5 Gamma Squeeze

Gamma 挤压发生在期权合约突然需求大增时：
1. 大量买入 Call → 造市商卖出 Call
2. 造市商需要买入股票对冲 → 推高股价
3. 股价上涨 → 更多 Call 被买入 → 循环加速
4. 最终造成价格井喷（如 GME 事件）

---

## 三、Delta 与 Gamma 的关系

$$\Delta_{\text{new}} \approx \Delta_{\text{current}} + \Gamma \cdot \Delta S$$

- Delta 是速度，Gamma 是加速度
- 线性 Gamma 近似只在小幅变动时准确
- 大幅变动时 Gamma 本身也在变，实际 Delta 会和线性估计有偏差

---

> [!seealso] 相关笔记
> - [[希腊字母总览]] — Greeks 速查表
> - [[Theta与Vega详解]] — 时间衰减与波动率
> - [[希腊字母Python实现]] — 代码计算
> - [[期权策略组合指南]] — 基于 Greeks 的策略构建
