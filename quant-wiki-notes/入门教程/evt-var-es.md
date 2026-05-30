---
title: "一文带你读懂金融市场尾部风险：极值理论（EVT）在VaR与ES计算中的应用"
category: "入门教程"
tags: [入门教程, 量化, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

# 一文带你读懂金融市场尾部风险：极值理论（EVT）在VaR与ES计算中的应用

## 极值理论（EVT）：尾部风险建模

在金融风险管理中，极值理论（EVT）是一种重要的工具，用于分析和建模数据分布的尾部行为。特别是在金融市场中，极端的市场波动和风险事件往往会导致巨大的经济损失，而极值理论能够帮助我们更好地理解和预测这些极端事件的发生概率及其影响。

## 极值理论的两种主要方法

极值理论的核心思想是对数据的极端值进行建模，通常有两种流行的参数化方法：**Block Maxima方法**和**Peak-Over-Threshold (POT) 方法**。

### Block Maxima方法

**Block Maxima**方法的基本思想是将历史数据分成多个块（例如按月、季度或年度），然后从每个块中提取最大值，这些最大值构成了我们用来建模尾部风险的样本。

假设我们有一些独立同分布（iid）随机变量，它们的累积分布函数为**F(x)**，并且有**n**个观测值。我们希望建模的是**Mₙ = max(X₁, X₂, ..., Xₙ)** 的统计行为。通过累积概率分布的关系，最大值的分布可以表示为：

$$
Pr(M_n \leq z) = Pr(X_1 \leq z, \ldots, X_n \leq z) = (F(z))^n
$$

然而，我们通常无法得到真实的分布函数F(x)。幸运的是，**Fisher-Tippett-Gnedenko定理**指出，对于适当的缩放，最大值的分布会收敛到三个特定的分布之一：**甘贝尔分布**、**弗雷歇分布**和**威布尔分布**。这些分布的组合形式为广义极值（GEV）分布：

$$
G(x) = \exp \left\{- \left[1 + \xi \left(\frac{x - \mu}{\sigma}\right)\right]^{-1/\xi}\right\}
$$

其中，**μ**是位置参数，**σ**是尺度参数，**ξ**是形状参数。不同的ξ值决定了尾部行为：

- 当**ξ = 0**时，得到甘贝尔分布（Gumbel）。
- 当**ξ < 0**时，得到弗雷歇分布（Fréchet）。
- 当**ξ > 0**时，得到威布尔分布（Weibull）。

通过使用R语言的`fExtremes`包，您可以绘制这些分布的密度图，帮助理解不同ξ值下的尾部行为。

![](https://fastly.jsdelivr.net/gh/bucketio/img17@main/2025/02/15/1739614133652-5a5c0ac5-0c4f-4bb7-a076-75928efb3481.png)

#### 数据拟合：块最大值方法

我们如何将广义极值（GEV）分布拟合到实际数据中呢？例如，在金融市场中，我们可以使用每日收益数据，将其分成每月的时间块，并对每个月的最大损失进行建模。这样，我们就能估计损失分布的尾部。

```r
require(quantmod)
require(xts)
SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- diff(log(SPY_prices), k = 1)[-1] * 100  # 每日对数收益
```

#### 转换为损失（负收益的正值），并计算每月最大损失

```r
monthly_max_daily_loss <- do.call(rbind, lapply(split(x = -1 * returns_xts, 'months'), function(x) x[which.max(x)]))
```
通过上述代码，我们将每日收益数据转换为每月的最大损失，进而利用最大似然估计（MLE）来拟合GEV分布参数。

估算风险：VaR和ES
通过拟合后的GEV分布参数，我们可以计算**VaR（价值风险）和ES（预期损失）** 等风险指标。例如，VaR可以通过逆累积分布函数计算：
```r
GEV_VAR <- function(params, alpha = .05){
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))
    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}
```
通过将拟合参数输入到VaR函数中，可以计算不同置信度下的VaR值。
```r
my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```
----

### Peak-Over-Threshold方法

**Peak-Over-Threshold (POT)** 方法与Block Maxima方法不同，它关注的是所有超过某个设定阈值的观测值。POT方法通常能更有效地捕捉尾部风险，尤其是在数据中存在多个极端值时。

在POT方法中，我们使用**广义帕累托分布（GPD）** 来描述超过阈值的观察值。通过**Pickands-Balkema-de Haan定理**，我们知道，对于足够大的阈值，数据的条件分布将近似为广义帕累托分布：

$$
P(X \leq x | X > u) \approx \left\{
\begin{array}{ll}
1 - \left( 1 + \xi \frac{x}{\tau} \right)^{-1/\xi} & \text{当} \xi \neq 0 \\
1 - \exp \left( -\frac{x}{\tau} \right) & \text{当} \xi = 0
\end{array}
\right.
$$

这里的参数**ξ**和**τ**与GEV分布的参数相似，用于拟合超过阈值的数据。

#### 数据拟合：POT方法

在使用POT方法时，我们首先设定一个阈值**u**，然后筛选出所有超过该阈值的观测值。接下来，我们拟合这些超过阈值的观测值，通常使用**广义帕累托分布（GPD）** 进行建模。

下面是用R语言拟合POT模型的代码示例，首先加载数据并设置阈值：

```r
require(quantmod)
require(xts)

SPY_prices <- Ad(getSymbols('SPY', from = '2006-01-01', to = '2019-01-01', auto.assign = FALSE))
returns_xts <- -1 * diff(log(SPY_prices), k = 1)[-1] * 100  # 每日对数收益
names(returns_xts) <- 'SPY_Returns'

# 设置阈值
my_threshold <- 0.85

# 筛选出超过阈值的数据
my_data <- returns_xts[returns_xts > my_threshold]
```
接下来，我们可以使用对数似然函数来进行参数估计：
```r
gdp_loglik <- function(params, threshold, data){
    xi <- params[1]; tau <- params[2]
    data <- data - threshold  # y = x - u
    data <- coredata(data[data > 0])  # 只保留超过阈值的数据
    m <- nrow(data)
    if((tau <= 0) | (xi <= -1)) return(1e6)  # 参数约束
    term1 <- -m * log(tau)
    if(abs(xi) < 0.0001){
        result <- term1 - 1 / tau * sum(data)
    } else {
        if(any(1 + xi * data / tau <= 0)) return(1e6)
        result <- term1 - (1 + 1 / xi) * sum(log(1 + xi * data / tau))
    }
    return(-result)
}
```
通过最大化对数似然函数，我们可以得到ξ和τ的估计值
```r
my_gpd_fit <- optim(par = c(0.5, 0.5), fn = gdp_loglik, method = "Nelder-Mead", threshold = my_threshold, data = returns_xts)
my_gpd_fit
```

### 计算风险：VaR和ES

通过拟合后的GEV分布参数，我们可以计算**VaR（价值风险）** 和**ES（预期损失）** 等风险指标。例如，VaR可以通过逆累积分布函数计算：

#### VaR（价值风险）计算

VaR是某个置信度下的分位数值。为了计算VaR，我们需要使用累积分布函数的逆函数。具体的公式如下：

$$
\hat{z}_p = \left\{
\begin{array}{ll}
\mu - \frac{\sigma}{\hat{\xi}} \left[ 1 - y_p^{-\xi} \right] & \text{当} \hat{\xi} \neq 0 \\
\hat{\mu} - \hat{\sigma} \log (-y_p) & \text{当} \hat{\xi} = 0
\end{array}
\right.
$$

其中，$y_p = -\log(1 - p)$，$p$为置信度（例如，0.05代表95%的置信区间）。

下面是计算VaR的R代码实现：

```r
GEV_VAR <- function(params, alpha = .05){
    # 将参数展开为向量
    mu    <- rep(params[1], length(alpha))
    sigma <- rep(params[2], length(alpha))
    xi    <- rep(params[3], length(alpha))

    y <- -log(1 - alpha)
    result <- ifelse(abs(xi) < 0.0001, mu - sigma * log(-y), mu - sigma / xi * (1 - y ^ -xi))
    return(result)
}
使用上述函数，可以计算不同置信度下的VaR值：
```r
my_fit_vals <- my_gev_fit$par
GEV_VAR(my_fit_vals, alpha = c(.05, .025, .01))
```
#### ES（预期损失）计算

**ES**（即条件VaR）表示在发生极端损失时，平均损失的大小。它反映了在损失超过VaR时，风险的严重程度。计算ES的公式如下：

$$
\mathrm{ES}_{\alpha} = \frac{1}{1 - \alpha} \int_{\alpha}^{1} q_x(F) \, \mathrm{d}x = \frac{VAR_{\alpha}}{1 - \xi} + \frac{\tilde{\sigma} - \xi u}{1 - \xi}
$$

其中，$\hat{z}_p$为VaR值，$\alpha$为风险水平（例如，0.01代表1%风险水平）。

在R语言中，计算ES的实现如下：

```r
GEV_ES <- function(params, alpha = .05){
    # 定义一个函数来计算VAR值
    my_fun <- function(x) {GEV_VAR(x, params = params)}

    # 数值积分，计算ES
    result <- 1 / alpha * integrate(my_fun, lower = .00001, upper = alpha, stop.on.error = FALSE)$value
    return(result)
}
```
通过上述代码，我们可以计算在特定置信度下的ES值。例如，对于1%的风险水平，我们可以运行：
```r
GEV_ES(my_fit_vals, alpha = .01)
```
这个计算结果告诉我们，在发生极端损失时，平均损失的大小。如果我们知道VaR为8.66%，ES的结果则可能会更大，因为ES考虑了更极端的损失情境。

通过使用ES，金融机构和投资者能够更好地评估风险，并准备应对极端市场波动时可能发生的更大损失。

## 总结

极值理论（EVT）为金融市场的尾部风险管理提供了强有力的工具，尤其是在面对市场极端波动时，能够帮助决策者制定更加合理的风险控制策略。通过**Block Maxima**和**Peak-Over-Threshold**两种方法，我们可以有效地估计尾部风险，并使用**广义极值分布（GEV）** 和**广义帕累托分布（GPD）** 进行拟合和风险评估。

在具体应用中，通过计算**VaR（价值风险）** 和**ES（预期损失）** 等风险指标，投资者和金融机构能够量化极端事件的影响，并采取相应的风险控制措施。VaR为特定置信水平下的潜在损失提供了一个界限，而ES则进一步考虑了极端损失的平均大小，帮助我们更好地理解尾部风险。
