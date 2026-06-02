---
title: Black-Scholes模型
tags:
  - Black-Scholes
  - 期权定价
  - BSM
  - 偏微分方程
  - 风险中性
created: 2026-06-02
source: 整合自多个来源
---

# Black-Scholes模型

> [!note] 核心要点
> Black-Scholes 模型是现代金融工程的奠基理论，通过随机微积分、无套利思想与资本市场均衡机制，构建出连续时间下欧式期权的封闭解定价公式。

---

## 一、模型背景

Black-Scholes 模型由 Fischer Black、Myron Scholes 和 Robert Merton 于 **1973 年**提出。该模型首次给出了一个封闭解公式，能够快速计算欧式期权的理论价格。

**重要意义**：
- 简化期权定价，提供精确的数学工具
- 推动衍生品市场发展
- 奠定金融数学基础

---

## 二、模型基本假设

1️⃣ **无风险利率恒定**：$r$ 在期权存续期内保持不变，按连续复利计息

2️⃣ **市场无摩擦**：不存在交易成本、税收及流动性限制

3️⃣ **标的资产无分红**：资产不支付分红（后续改进可引入股息）

4️⃣ **连续交易与动态对冲**：投资者可随时调整持仓

5️⃣ **不存在套利机会**：市场价格处于均衡状态

6️⃣ **资产价格服从几何布朗运动**：

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

其中 $\mu$ 为预期收益率，$\sigma$ 为波动率，$W_t$ 为标准布朗运动。

---

## 三、BSM 定价公式

### 欧式看涨期权

$$C = S_0 N(d_1) - K e^{-rT} N(d_2)$$

### 欧式看跌期权

$$P = K e^{-rT} N(-d_2) - S_0 N(-d_1)$$

### 其中

$$d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$$

$$d_2 = d_1 - \sigma\sqrt{T}$$

$N(\cdot)$ 为标准正态分布的累积分布函数。

> [!tip] 公式直觉理解
> - $S_0 \cdot N(d_1)$：标的资产上涨到期权内在价值的概率加权现值
> - $K e^{-rT} \cdot N(d_2)$：行权时支付行权价的概率加权现值
> - $N(d_2)$：风险中性测度下期权到期实值的概率

---

## 四、推导思路

### 4.1 无风险对冲组合

构造组合：$\Pi = C - \Delta S$

对 $C(S,t)$ 应用伊藤引理：

$$dC = \frac{\partial C}{\partial t}dt + \frac{\partial C}{\partial S}dS + \frac{1}{2}\frac{\partial^2 C}{\partial S^2}(dS)^2$$

若取 $\Delta = \frac{\partial C}{\partial S}$，则随机项 $dW_t$ 被完全消除。

### 4.2 Black-Scholes 偏微分方程

$$\frac{\partial C}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} + rS\frac{\partial C}{\partial S} - rC = 0$$

结合边界条件 $C(T) = \max(S_T - K, 0)$，即可求得封闭解。

### 4.3 风险中性定价

在风险中性世界中：
- 资产预期收益率 $\mu$ 被替换为无风险利率 $r$
- 投资者风险偏好被"剥离"
- 不确定性通过波动率 $\sigma$ 体现

> [!important] 核心思想
> Black-Scholes 模型的核心不是预测未来价格，而是衡量在不确定性条件下的**合理风险补偿**。

---

## 五、含股息的扩展

引入股息收益率 $q$：

$$C = S_0 e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$

$$d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}$$

---

## 六、模型的局限性

| 局限 | 说明 |
|------|------|
| 恒定波动率 | 市场中波动率常随时间和价格变化（波动率微笑） |
| 忽略极端事件 | 假设价格变化连续，但实际可能发生跳跃 |
| 理想化假设 | 忽略交易成本、税收及流动性问题 |
| 不考虑股息 | 原始模型未考虑分红 |

### 改进方向

- **随机波动率模型**：如 Heston 模型
- **跳跃扩散模型**：如 Merton 跳跃模型
- **含分红模型**：引入股息收益率 $q$

---

## 七、Python 计算示例

```python
import numpy as np
from scipy.stats import norm

S0, K, T, r, sigma = 100, 105, 0.5, 0.05, 0.30

d1 = (np.log(S0/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
d2 = d1 - sigma*np.sqrt(T)
C = S0*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)

print(f"期权价格 C ≈ {C:.2f}")  # ≈ 6.86
```

---

> [!seealso] 相关笔记
> - [[期权基础概念]] — 期权定义与类型
> - [[希腊字母总览]] — BSM 框架下的 Greeks
> - [[二叉树定价模型]] — BSM 的离散近似
> - [[三大定价模型对比]] — 与其他模型的比较
