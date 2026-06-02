---
title: 期权Greeks风控
aliases: [Option Greeks, Delta, Gamma, Vega, Theta, 期权风险管理]
tags: [风险控制, 期权, Greeks, Delta, Gamma, Vega]
created: 2026-06-02
source: CME/NACC综合
---

# 期权Greeks风控

> [!note] 核心要点
> 期权Greeks是衡量期权价格对各种因素敏感度的风险指标。掌握Delta、Gamma、Vega、Theta等Greeks的含义和管理方法，是期权交易风控的基础。

## 一、Greeks指标体系

### 1.1 Delta (Δ)

$$\Delta = \frac{\partial V}{\partial S}$$

- 衡量期权价格对**标的价格**的敏感度
- 看涨期权：0 ≤ Δ ≤ 1
- 看跌期权：-1 ≤ Δ ≤ 0
- **Delta对冲**：持有Δ份标的资产对冲期权头寸

### 1.2 Gamma (Γ)

$$\Gamma = \frac{\partial^2 V}{\partial S^2} = \frac{\partial \Delta}{\partial S}$$

- 衡量Delta对标的价格的**变化率**
- 平值期权Gamma最大
- Gamma大 = Delta变化快 = 需要频繁对冲

### 1.3 Vega (ν)

$$\nu = \frac{\partial V}{\partial \sigma}$$

- 衡量期权价格对**波动率**的敏感度
- 长期平值期权Vega最大
- 做多Vega = 波动率上升时盈利

### 1.4 Theta (Θ)

$$\Theta = \frac{\partial V}{\partial t}$$

- 衡量期权价格对**时间**的敏感度
- 通常为负值（时间衰减）
- 临近到期时Theta衰减加速

### 1.5 Rho (ρ)

$$\rho = \frac{\partial V}{\partial r}$$

- 衡量期权价格对**利率**的敏感度
- 长期期权Rho影响较大

## 二、Greeks汇总

| Greek | 衡量对象 | 公式 | 典型特征 |
|-------|----------|------|----------|
| Delta | 标的价格 | ∂V/∂S | 平值≈0.5 |
| Gamma | Delta变化 | ∂²V/∂S² | 平值最大 |
| Vega | 波动率 | ∂V/∂σ | 长期平值最大 |
| Theta | 时间衰减 | ∂V/∂t | 通常为负 |
| Rho | 利率 | ∂V/∂r | 长期期权敏感 |

## 三、风险管理策略

### 3.1 Delta中性

- 目标：组合Delta = 0
- 方法：动态调整标的持仓
- 频率：取决于Gamma大小

### 3.2 Gamma对冲

- 高Gamma = 需要频繁再平衡
- 使用期权对冲Gamma风险
- 成本与精度的权衡

### 3.3 Vega对冲

- 使用不同期限期权对冲
- 关注波动率曲面变化
- 日历价差策略

### 3.4 Theta管理

- 卖方策略：正Theta（时间衰减收益）
- 买方策略：负Theta（时间衰减成本）
- Theta与Gamma的权衡

## 四、组合Greeks管理

$$\text{组合Greek} = \sum_i n_i \cdot \text{Greek}_i$$

其中 $n_i$ 是第i个头寸的数量。

### 实战要点

1. **动态对冲**：根据Greeks变化实时调整
2. **情景分析**：模拟标的价格、波动率、时间同时变化
3. **压力测试**：极端行情下Greeks的非线性变化

## 相关链接
- [[风险度量指标]] — 组合层面风险度量
- [[量化风险管理体系]] — 完整风控框架
- [[黑天鹅风险管理]] — 极端行情期权对冲
