---
title: 希腊字母Python实现
tags:
  - Python
  - 希腊字母
  - Greeks
  - BSM
  - 代码实现
created: 2026-06-02
source: 整合自多个来源
---

# 希腊字母Python实现

> [!note] 核心要点
> Greeks 的计算有两种方式：解析解（直接求偏导）和差分法（数值近似）。解析解最准确最快，但蒙特卡洛等无解析解的情况只能用差分法。

---

## 一、解析解计算方式

### 1.1 BSM Greeks 公式

基于广义 BSM 公式：

$$C = S_0 e^{(b-r)T} N(d_1) - K e^{-rT} N(d_2)$$

其中 $b$ 为持有成本参数：
- $b = r$：标准无股利模型
- $b = 0$：期货期权
- $b = r - q$：支付股利 $q$ 的期权
- $b = r - r_f$：外汇期权

### 1.2 Python 实现代码

```python
import numpy as np
from scipy.stats import norm

class BSMCalculator:
    """Black-Scholes-Merton 期权定价与 Greeks 计算"""
    
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        self.d2 = self.d1 - sigma*np.sqrt(T)
    
    def call_price(self):
        return self.S*norm.cdf(self.d1) - self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)
    
    def put_price(self):
        return self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2) - self.S*norm.cdf(-self.d1)
    
    def delta(self, option_type='call'):
        if option_type == 'call':
            return norm.cdf(self.d1)
        return norm.cdf(self.d1) - 1
    
    def gamma(self):
        return norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.T))
    
    def theta(self, option_type='call'):
        """返回每日 Theta（年化值除以 365）"""
        common = -self.S*norm.pdf(self.d1)*self.sigma / (2*np.sqrt(self.T))
        if option_type == 'call':
            return (common - self.r*self.K*np.exp(-self.r*self.T)*norm.cdf(self.d2)) / 365
        return (common + self.r*self.K*np.exp(-self.r*self.T)*norm.cdf(-self.d2)) / 365
    
    def vega(self):
        """返回每 1% 波动率变化的价格变动"""
        return self.S * norm.pdf(self.d1) * np.sqrt(self.T) / 100
    
    def rho(self, option_type='call'):
        """返回每 1% 利率变化的价格变动"""
        if option_type == 'call':
            return self.K*self.T*np.exp(-self.r*self.T)*norm.cdf(self.d2) / 100
        return -self.K*self.T*np.exp(-self.r*self.T)*norm.cdf(-self.d2) / 100

# 示例：S=100, K=100, T=0.25(90天), r=5%, sigma=25%
bsm = BSMCalculator(S=100, K=100, T=0.25, r=0.05, sigma=0.25)
print(f"Call Price:  {bsm.call_price():.4f}")   # 5.5984
print(f"Put Price:   {bsm.put_price():.4f}")    # 4.3562
print(f"Call Delta:  {bsm.delta('call'):.4f}")  # 0.5645
print(f"Put Delta:   {bsm.delta('put'):.4f}")   # -0.4355
print(f"Gamma:       {bsm.gamma():.4f}")        # 0.0315
print(f"Call Theta:  {bsm.theta('call'):.4f}")  # -0.0339
print(f"Vega:        {bsm.vega():.4f}")         # 0.1969
print(f"Call Rho:    {bsm.rho('call'):.4f}")    # 0.1271
```

### 1.3 广义 BSM 的 Greeks 函数

```python
def greeks(CP, S, X, sigma, T, r, b):
    """
    计算广义 BSM 的 Greeks
    CP: "C" 看涨, "P" 看跌
    b: 持有成本参数
    """
    d1 = (np.log(S/X) + (b + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    if CP == "C":
        option_value = S*np.exp((b-r)*T)*norm.cdf(d1) - X*np.exp(-r*T)*norm.cdf(d2)
        delta = np.exp((b-r)*T) * norm.cdf(d1)
        theta = (-np.exp((b-r)*T)*S*norm.pdf(d1)*sigma/(2*T**0.5) 
                 - r*X*np.exp(-r*T)*norm.cdf(d2) 
                 - (b-r)*S*np.exp((b-r)*T)*norm.cdf(d1))
    else:
        option_value = X*np.exp(-r*T)*norm.cdf(-d2) - S*np.exp((b-r)*T)*norm.cdf(-d1)
        delta = -np.exp((b-r)*T) * norm.cdf(-d1)
        theta = (-np.exp((b-r)*T)*S*norm.pdf(d1)*sigma/(2*T**0.5) 
                 + r*X*np.exp(-r*T)*norm.cdf(-d2) 
                 + (b-r)*S*np.exp((b-r)*T)*norm.cdf(-d1))
    
    gamma = np.exp((b-r)*T) * norm.pdf(d1) / (S*sigma*T**0.5)
    vega = S * np.exp((b-r)*T) * norm.pdf(d1) * T**0.5
    
    if b != 0:
        rho = X*T*np.exp(-r*T)*norm.cdf(d2) if CP=="C" else -X*T*np.exp(-r*T)*norm.cdf(-d2)
    else:
        rho = -T*np.exp(-r*T)*(S*norm.cdf(d1)-X*norm.cdf(d2)) if CP=="C" else \
              -T*np.exp(-r*T)*(X*norm.cdf(-d2)-S*norm.cdf(-d1))
    
    return {"option_value": option_value, "delta": delta, "gamma": gamma,
            "vega": vega, "theta": theta, "rho": rho}
```

---

## 二、差分计算方式

对于蒙特卡洛模拟和有限差分等无解析解的情况，使用差分法近似：

```python
def greeks_diff(CP, S, X, sigma, T, r, b, pct_change=0.0001):
    """差分方式计算 Greeks"""
    f = lambda s, t: BSM(CP, s, X, sigma, t, r, b)
    
    delta = (f(S+S*pct_change, T) - f(S-S*pct_change, T)) / (2*S*pct_change)
    gamma = (f(S+S*pct_change, T) + f(S-S*pct_change, T) - 2*f(S, T)) / (S*pct_change)**2
    vega = (f(S, T) - f(S, T))  # 类似方式对 sigma 求差分
    theta = (f(S, T-T*pct_change) - f(S, T+T*pct_change)) / (2*T*pct_change)
    
    return {"delta": delta, "gamma": gamma, "vega": vega, "theta": theta}
```

> [!tip] 差分法要点
> - `pct_change` 通常取万分之一（0.0001）
> - 中间差分比前向差分更准确
> - 解析解和差分法的结果基本一致，可互相验证

---

## 三、牛顿法求解隐含波动率

利用 Vega 加速隐含波动率求解：

```python
def newton_imp_vol(C0, CP, S, X, T, r, b, vol_est=0.25, n_iter=1000):
    """牛顿法求解隐含波动率"""
    for i in range(n_iter):
        d1 = (np.log(S/X) + (b + vol_est**2/2)*T) / (vol_est*np.sqrt(T))
        vega = S * np.exp((b-r)*T) * norm.pdf(d1) * T**0.5
        vol_est = vol_est - (BSM(CP, S, X, vol_est, T, r, b) - C0) / vega
    return vol_est
```

> [!note] 牛顿法 vs 二分法
> 牛顿法利用 Vega 作为导数，收敛速度比二分法更快。

---

> [!seealso] 相关笔记
> - [[希腊字母总览]] — Greeks 理论基础
> - [[Black-Scholes模型]] — BSM 公式推导
> - [[二叉树定价模型]] — 数值方法
