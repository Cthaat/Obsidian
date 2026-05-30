---
title: "2024年AI量化论文优选"
category: "AI+量化"
tags: [AI+量化, 量化, 交易, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

# 2024年AI量化论文优选

本篇汇总收录了共计 **41 篇**（精选及拓展阅读）定量金融领域的**前沿研究成果**。这些论文涵盖了从股票、外汇、商品、固定收益与信用市场到投资组合优化、市场预测、衍生品建模、宏观经济与地缘政治风险，以及加密货币与 DeFi 等多元主题。尤其值得关注的是，越来越多的工作正将人工智能（AI）与大型语言模型（LLMs）引入金融分析与交易中，不仅提升预测与评估的精准度和效率，还为策略制定、投资决策与风险管理提供了全新思路。

本文所选论文横跨多种资产类别与研究方向，包括但不限于以下重点领域：

- **AI 与 LLM 在金融中的应用**：利用 LLM 微调、提示工程、多模态 Transformer 及扩散模型应对数据不平衡和复杂预测挑战。
- **市场微观结构与流动性分析**：针对 LOB、自动做市商（AMM）、价格冲击与市场脆弱性问题提出新的理论与实证研究。
- **风险管理与政策制定参考**：从 ESG 投资的多智能体强化学习模型到地缘政治风险、信用与宏观波动下的量化风险评估工具，为政策与投资策略提供实用指南。
- **衍生品与波动率建模**：借助深度学习与可解释性分析，提高粗糙波动模型、期权定价及高频预测方法的精确度与可理解度。

通过这份精选列表，研究者、从业者与学生可迅速了解定量金融与 AI 技术交织下的最新研究趋势、方法与应用场景，为未来的实务与学术探索提供参考与灵感。

## 内容目录

### AI and LLMs in Financial Analysis and Trading

1. **CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction**
2. **FinRobot: AI Agent for Equity Research and Valuation with Large Language Models**
3. **FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading**
4. **AI in Investment Analysis: LLMs for Equity Stock Ratings**
5. **Adaptive and Explainable Margin Trading Via Large Language Models on Portfolio Management**
6. **Modality-aware Transformer for Financial Time series Forecasting**
7. **Imb-FinDiff: Conditional Diffusion Models for Class Imbalance Synthesis of Financial Tabular Data**
8. **InvestESG: A multi-agent Reinforcement Learning Benchmark for Studying Climate Investment As a Social Dilemma**

### Stock Market, Equity Market

9. **You Can Only Lend What You Own: Inferring Daily Institutional Trading from Security Lending Supply**
10. **Factor Momentum Versus Price momentum: Insights from International Markets**
11. **National Culture of Secrecy and Stock Price synchronicity: Cross-country Evidence**
12. **Asset Pricing in African Frontier Equity Markets**

### FX (Foreign Exchange)

13. **What Events Matter for Exchange Rate volatility?**
14. **How Institutions Interact with Exchange Rates After the 2024 US Presidential Election: New High-frequency evidence**

### Commodity Market

15. **Extrapolating the long-term Seasonal Component of Electricity Prices for Forecasting in the day-ahead Market**

### Fixed Income and Bonds Markets

16. **Real-world Models for Multiple Term structures: a Unifying HJM Framework**

### Credit Markets

17. **The Pricing of Asset-Backed Securities and Households’ Pecking Order of Debt**
18. **Information Span and Credit Market Competition**

### Portfolio Optimization and Market Prediction

19. **The M6 Forecasting competition: Bridging the Gap Between Forecasting and Investment Decisions**
20. **Cluster-driven Hierarchical Representation of Large Asset Universes for Optimal Portfolio Construction**
21. **Interpretable Machine Learning Model for Predicting Activist Investment Targets**

### Electronic Financial Markets and Limit Order Books (LOB)

22. **Efficient Trading with Price Impact**
23. **Market Making Without Regret**
24. **Through Stormy seas: How Fragile Is Liquidity Across Asset Classes and time?**

### Derivative Modeling and Volatility

25. **Deep Learning Interpretability for Rough Volatility**
26. **Stable Multilevel Deep Neural Networks for Option Pricing and xVAs Using Forward-Backward Stochastic Differential Equations**
27. **Beyond the Traditional VIX: A Novel Approach to Identifying Uncertainty Shocks in Financial Markets**
28. **Short-maturity Options on Realized Variance in local-stochastic Volatility Models**

### Financial Markets, Economics, Game Theory, and Macroeconomics

29. **Stochastic Graphon Games with Memory**
30. **AI-generated production networks: Measurement and applications to global trade**
31. **Rg Before and After the Great Wars 1507-2023**
32. **Firm Heterogeneity and Macroeconomic Fluctuations: a Functional VAR Model**
33. **Taming Data Driven Probability Distributions**

### Quantitative Risk Management

34. **D5.12: Evaluation of Quantum Algorithms for Finance**
35. **An Empirical Implementation of the Shadow Riskless Rate**
36. **Efficient Nested Estimation of CoVaR: A Decoupled Approach**
37. **Volatility Connectedness Between Geopolitical Risk and Financial markets: Insights from Pandemic and Military Crisis Periods**
38. **Cross-quantile Risk assessment: the Interplay of Crude oil, Artificial intelligence, Clean tech, and Other Markets**

### Cryptocurrencies and Decentralized Finance (DeFi)

39. **Strategic Bonding Curves in Automated Market Makers**
40. **Price Divergence in Bitcoin Market**
41. **Automated Market Making: the case of Pegged Assets**

---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/12/14/1734212989861-3c489e88-e079-41b1-bf7d-c78ebe47a3be.png)

## 精华解读

#### CausalStock: Deep End-to-end Causal Discovery for News-driven Stock Movement Prediction

S Li, Y Sun, Y Lin, X Gao, S Shang, R Yan - arXiv preprint arXiv, 2024 - arxiv.org
北京大学、人民大学

![](https://fastly.jsdelivr.net/gh/bucketio/img1@main/2024/12/14/1734213395814-6b4e7dd7-3b10-4a81-b636-34d9269b3d34.png)

**结果 - 主要发现**
通过在股票间发现时间因果关系并采用先进模型，CausalStock 在全球市场的多股票走势预测上超越现有方法。

- 利用 Functional Causal Model 并引入时滞相关的时间因果发现机制，更适用于股票时间序列数据。
- 使用 Denoised News Encoder（基于LLM）从噪声新闻中提取有效信息，结合神经网络与变分推断进行预测。
- 对美国、中国、日本和英国市场数据测试，CausalStock 表现优于现有方法，预测清晰可解释，有助于金融分析与量化交易。

---

#### FinRobot: AI Agent for Equity Research and Valuation with Large Language Models

T Zhou, P Wang, Y Wu, H Yang - arXiv:2411.08804, 2024 - arxiv.org
AI4Finance Foundation, Brown University

![Overall Framework of FinRobot](https://fastly.jsdelivr.net/gh/bucketio/img14@main/2024/12/14/1734213424420-e6e238a4-fa44-4266-b469-e3c75900863e.png)

**结果 - 主要发现**
FinRobot引入首个面向股权研究的AI Agent框架，采用多智能体链式思考，将定量与定性分析相结合，模拟人类分析师推理。

- 多智能体CoT框架（Data-CoT、Concept-CoT、Thesis-CoT）综合人类分析师思维过程。
- 整合定量定性分析与实时数据，引入新评估指标（Accuracy、Logicality、Storytelling）提升报告质量与时效性。
- 开源FinRobot，促进金融领域高级AI工具的普及与协作。

---

#### FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading

G Iacovides, T Konstantinidis, M Xu, D Mandic - ACM AI in Finance, 2024
帝国理工学院

![Training parameters used in the fine-tuning process of the proposed FinLlama](https://fastly.jsdelivr.net/gh/bucketio/img7@main/2024/12/14/1734213454721-b7a119f1-8d2c-441c-a0b4-998054d31ab4.png)

**结果 - 主要发现**
对 Llama 2 进行金融情感微调的 FinLlama 提升算法交易绩效。

- 基于标注金融文本数据微调Llama 2 (7B)模型，可准确分类情感及其强度。
- 利用LoRA与8位量化降低计算要求，无需昂贵硬件保持高准确度。
- 投资组合模拟中，FinLlama优于FinBERT等现有方法，在波动市场中表现更稳健。

---

#### AI in Investment Analysis: LLMs for Equity Stock Ratings

K Papasotiriou, S Sood, S Reynolds, T Balch - ACM AI in Finance, 2024
J.P. Morgan AI Research, Emory大学

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2024/12/14/1734213477673-6b5bd1db-04e3-4b6f-b8c0-094ae776a3a2.png)

**结果 - 主要发现**
借助GPT-4与金融数据，LLM 在股票评级预测中优于传统分析师。

- 利用GPT-4-32k对S&P500公司进行评级预测，结合财务、市场与新闻数据，预测未来收益表现优于分析师评级。
- 融合财务基本面可显著提高准确度；使用新闻情感替代详细摘要可减少Token消耗且不降低性能。
- LLM可高效整合多模态数据，为传统评级方法提供低成本高效替代方案。

---

#### Adaptive and explainable margin trading via large language models on portfolio management

J Gu, J Ye, G Wang, W Yin - ACM AI in Finance, 2024
新泽西理工、宾州州立

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/12/14/1734213497508-c1cf6bea-352b-4d5a-8bea-f5d0a8f1008a.png)

**结果 - 主要发现**
LLM结合强化学习动态调整仓位，提高投资组合收益与夏普比率。

- 两阶段框架（可解释市场预测/推理+头寸再分配）比基准收益提升三倍、夏普比率翻倍。
- 使用LLM处理多源数据预测市场趋势并动态调仓，提高盈利与风险管理。
- 展示LLM 在策略透明性与适应性方面的潜力。

---

#### Modality-aware Transformer for Financial Time series Forecasting

H Emami Gohari et al. - ACM AI in Finance, 2024
IBM T.J Watson

![The Modality-aware Transformer (MAT) employs Intra-modal, Inter-modal, and Target-modal MHA, fused via feature-level attentions. This enhances temporal attention, leveraging modality and feature importance for richer embeddings. MAT’s design optimizes information use across and within modalities](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2024/12/14/1734213532472-1acc97b2-6bee-4932-9ddd-618fbc123efb.png)

**结果 - 主要发现**
MAT模型融合文本报告与数值数据，提高金融时间序列预测精度。

- 特征级注意力层聚焦最有信息量的特征，提升准确度并可解释性。
- Intra-modal、Inter-modal、Target-modal注意力机制捕捉时间与跨模态依赖。
- 实证结果显著优于现有方法，为多模态预测提供有效解决方案。

---

#### Imb-FinDiff: Conditional Diffusion Models for Class Imbalance Synthesis of Financial Tabular Data

M Schreyer et al. - ACM AI in Finance, 2024  LBNL、ICSI

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/14/1734213579404-5bf29e79-e5eb-480d-b9a6-c072045ba5a7.png)

**结果 - 主要发现**
Imb-FinDiff通过扩散模型合成少数类样本，提高不平衡数据分类性能。

- 双重学习目标结合扩散噪声与类别预测，提升少数类合成质量。
- 相比SMOTE、ADASYN表现更佳，适用于混合类型表格数据。
- 实证证明在真实数据中具备高保真度与多样性。

---

#### InvestESG: A multi-agent reinforcement learning benchmark for studying climate investment as a social dilemma

X Hou et al. - arXiv:2411.09856, 2024
华盛顿大学、Google Deepmind

![](https://fastly.jsdelivr.net/gh/bucketio/img6@main/2024/12/14/1734213601249-f2cbdb5f-f8c9-45c9-992f-452e835cc0e6.png)

**结果 - 主要发现**
ESG投资者临界质量可促进企业气候缓解合作，MARL模拟显示信息透明可激励更多减缓投资。

- 强调ESG披露与知情投资者对企业行动的推动作用。
- MARL框架模拟公司-投资者互动，帮助政策制定与市场设计。
- 强调为系统披露全球气候风险信息的重要性。

---

#### You can only lend what you own: Inferring daily institutional trading from security lending supply

YH Barardehi et al. - SSRN, 2024
美国SEC、Chapman大学

**结果 - 主要发现**
可出借股份变动是机构交易可靠代理，比现有替代指标更准确。

- 可出借股份变动能更好追踪机构持仓变化。
- 该代理度量的机构交易负向预测股票收益，机构在盈余公告与拆股前做战略调整。
- 为理解机构行为与市场动态提供新工具。

---

#### Factor momentum versus price momentum: Insights from international markets

N Cakici et al. - Journal of Banking & Finance, 2024
Fordham大学、Montpellier商学院

**结果 - 主要发现**
因子动量在全球稳健但无法全面解释股票动量，动量为独立异象。

- 因子动量在全球市场强劲且独立于常见预测因子。
- 无法完全解释股票与行业动量，表明动量具独特性。
- 对投资管理与风险评估有启示意义。

---

#### National culture of secrecy and stock price synchronicity: Cross-country evidence

C Gaganis et al. - Journal of Banking & Finance, 2024
克里特大学、雅典经济与商业大学

**结果 - 主要发现**
文化保密性降低投资者信息搜寻，提高股价同步性、降低特异波动率。

- 秘密社会中投资者不积极信息搜寻，导致股价更具共动性。
- 内幕交易法执行可减少私有信息交易与特异波动性。
- 对理解文化因素对市场影响有重要意义。

---

#### Asset pricing in African frontier equity markets

B Hearn et al. - International Review of ..., 2024
南安普敦大学

**结果 - 主要发现**
传统定价模型不适用于非洲前沿市场，需要本土化定制模型。

- 分析表明当地主导条件影响定价结果，传统模型偏差明显。
- 为新兴经济体资产定价研究提供基础。

---

#### What events matter for exchange rate volatility?

I Martins, HF Lopes - arXiv:2411.16244, 2024
INSPER、厄勒布鲁大学

**结果 - 主要发现**
纳入与泰勒规则相关的宏观事件可提高汇率波动预测与投资组合性能。

- 新模型优于传统SV、GARCH模型。
- 分析澳元高频数据揭示W形日内季节性。

---

#### How Institutions Interact with Exchange Rates After the 2024 US Presidential Election: New High-frequency evidence

J Aizenman, J Saadaoui - NBER, 2024
USC、NBER、Paris 8

**结果 - 主要发现**
2024年美总统大选后，制度评分更高的国家货币对美元贬值更显著。

- 贬值与制度评分正相关，贸易盈余与汇率干预亦有影响。
- EIU的特朗普风险指数影响短期汇率动态。

---

#### Extrapolating the long-term seasonal component of electricity prices for forecasting in the day-ahead market

K Chec et al. - 2024
弗罗茨瓦夫理工

**结果 - 主要发现**
分解长期季节性成分提高电力日间市场预测精度与交易利润。

- 自回归与LASSO建模RMSE改善3%-15%。
- 提升策略盈利能力。

---

#### Real-world Models for Multiple Term structures: a Unifying HJM Framework

C Fontana et al. - arXiv:2411.01983, 2024
帕多瓦大学、悉尼科技大学

**结果 - 主要发现**
统一HJM框架处理多期限结构，确保无套利与市场可行性。

- 引入SPDE研究多期限结构，给出存在唯一性条件。
- 强调漂移限制对市场可行性的必要性。

---

#### The Pricing of Asset-Backed Securities and Households’ Pecking Order of Debt

R Füß et al. - Swiss Finance Institute, 2024
圣加仑大学

**结果 - 主要发现**
家庭债务排序影响ABS与RMBS定价与评级迁移。

- 理解消费者债务模式有助于预测ABS与RMBS表现。
- 提供新方法评估风险与收益。

---

#### Information Span and Credit Market Competition

Z He et al. - NBER, 2024
斯坦福大学、NYU Stern

**结果 - 主要发现**
信息跨度增强信贷市场竞争，让消费者获益。

- 信息可用性决定市场行为与效率。
- 为政策与金融决策提供参考。

---

#### The M6 Forecasting competition: Bridging the Gap Between Forecasting and Investment Decisions

S Makridakis et al. - arXiv, 2023
尼科西亚大学、雅典理工

**结果 - 主要发现**
M6竞赛显示预测难度大，但整合多重预测与集体智慧可提升投资绩效。

- 少数团队超过简单基准。
- 结合多预测与信息交换改进结果。

---

#### Cluster-driven Hierarchical Representation of Large Asset Universes for Optimal Portfolio Construction

N Khelifa et al. - ACM AI in Finance, 2024
牛津大学、图灵研究所

**结果 - 主要发现**
有符号谱聚类降维相关矩阵，提升组合构建表现。

- 新策略优于传统基准，更高夏普比率。
- 簇数量与预测质量至关重要。

---

#### Interpretable machine learning model for predicting activist investment targets

M Kim et al. - Journal of Finance and Data Science, 2024
爱丁堡大学、NYU阿布扎比

**结果 - 主要发现**
可解释逻辑回归模型预测激进投资目标，AUC-ROC=0.782。

- 使用SHAP解释特征重要性。
- 有助公司与投资者预判股东行动。

---

#### Efficient Trading with Price Impact

X Brokmann et al. - SSRN, 2024
帝国理工、LSE

**结果 - 主要发现**
线性反馈策略在非线性价格冲击模型中与神经网络策略性能相近，简单可解释。

- 平衡预期收益、风险与交易成本。
- 简洁稳健的替代方案。

---

#### Market Making without Regret

N Cesa-Bianchi et al. - arXiv, 2024
米兰大学、米兰理工

**结果 - 主要发现**
无遗憾市场做市元算法，在特定条件下O(T^(2/3))遗憾度。

- 同时讨论反馈模型下信息与遗憾权衡。
- 为在线学习策略提供新视角。

---

#### Through Stormy seas: How Fragile Is Liquidity Across Asset Classes and time?

N Aliyev et al. - BIS, 2024

**结果 - 主要发现**
过去25年全球流动性平均改善，但股票和债券市场流动性更脆弱。

- 买卖价差均值和标准差下降，但偏度峰度上升。
- 外汇市场未出现同样脆弱性。

---

#### Deep Learning Interpretability for Rough Volatility

B Yuan et al. - arXiv:2411.19317, 2024
剑桥、帝国理工、图灵所

**结果 - 主要发现**
可解释性分析揭示粗糙Heston模型标定中神经网络关注短期深实值期权隐含波动。

- 提升DL在量化金融中使用的安全性。
- 展现粗糙波动模型与经典模型差异。

---

#### Stable Multilevel Deep Neural Networks for Option Pricing and xVAs Using FBSDEs

A Ashok Naarayan, P Parpas - ACM AI in Finance, 2024
帝国理工

**结果 - 主要发现**
多层DNN架构灵感来自多层MC和FBSDE，大幅提高期权定价与xVA计算效率。

- NAIS-Net确保稳定性。
- 显著优于现有方法，提高准确度与速度。

---

#### Beyond the Traditional VIX: A Novel Approach to Identifying Uncertainty Shocks in Financial Markets

A Jha et al. - arXiv, 2024
德州理工、约翰霍普金斯

**结果 - 主要发现**
VVIX基于双重从属正态逆高斯过程，更准确衡量市场重尾与偏度特征。

- 弥补VIX缺陷，捕捉长记忆与不对称性。
- 加深对宏观不确定性冲击的理解。

---

#### Short-maturity options on realized variance in local-stochastic Volatility Models

D Pirjol et al. - arXiv:2411.02520, 2024
史蒂文斯理工、佛州立

**结果 - 主要发现**
导出局部-随机波动模型下方差期权短期渐近解，提供实践定价指南。

- 方差期权等价亚洲期权的分析。
- 数值模拟与理论结果一致。

---

#### Stochastic Graphon Games with Memory

E Neuman, S Tuschmann - arXiv:2411.05896, 2024
帝国理工

**结果 - 主要发现**
求解有记忆的随机Graphon博弈获显式纳什均衡，有限玩家均衡随玩家数增长收敛于Graphon均衡。

- 提供谱分解与收敛率分析。
- 理解大规模异质主体博弈。

---

#### AI-generated production networks: Measurement and applications to global trade

T Fetzer et al. - 2024
LSE、华威、帝国理工

![](https://fastly.jsdelivr.net/gh/bucketio/img19@main/2024/12/14/1734213697580-5ad13d3f-2b49-400a-ad03-a90e4367b6a4.png)

**结果 - 主要发现**
AIPNET利用生成式AI测绘5000+产品投入产出关系，揭示全球贸易格局改变。

- 显示供应冲击下的“回流”现象。
- 对政策制定与国际贸易分析有参考价值。

---

#### rg before and after the Great Wars 1507-2023

KS Rogoff, P Schmelzing - NBER, 2024
哈佛、波士顿学院

**结果 - 主要发现**
500年数据洞察r-g利差长期特征及重大事件影响。

- 历史视角揭示经济长期趋势。
- 对经济预测与政策有重要启示。

---

#### Firm Heterogeneity and Macroeconomic Fluctuations: a Functional VAR model

M Marcellino et al. - arXiv:2411.05695, 2024
博科尼大学

**结果 - 主要发现**
FunVAR模型捕捉TFP冲击对宏观与企业资本、劳动力分布影响。

- 采用张量降维技术模型企业异质性。
- 实证验证模型有效性。

---

#### Taming Data Driven Probability Distributions

J Baruník, L Hanus - Journal of Forecasting, 2024
查尔斯大学、捷克科学院

**结果 - 主要发现**
深度学习提高宏观与金融时间序列预测精度，可处理厚尾与不对称特征。

- 加强概率预测能力与决策辅助。
- 在两个数据集上验证有效性。

---

#### Evaluation of quantum algorithms for finance

A Manzano et al. - neasqc.eu
拉科鲁尼亚大学

**结果 - 主要发现**
QAMC与QML在金融应用中有进展，但量子硬件限制仍待突破。

- 开发QQuantLib工具库。
- 需进一步硬件与算法发展。

---

#### An Empirical Implementation of the Shadow Riskless Rate

D Lauria et al. - Risks, 2024
德州理工、约翰霍普金斯

**结果 - 主要发现**
利用PCA与SVD估计Shadow Riskless Rate，为投资分析与资产区分提供新工具。

- 改善市场中无风险率的度量问题。
- 有助资产类别区分与金融稳定评估。

---

#### Efficient Nested Estimation of CoVaR: A Decoupled Approach

N Lin et al. - arXiv:2411.01319, 2024
上交、复旦

**结果 - 主要发现**
分离事件处理与重定价，用平滑技术提高CoVaR估计效率与收敛率。

- 对比多种平滑技术，OP(n−1/2)收敛率。
- 实验验证方法实用性。

---

#### Volatility connectedness between geopolitical risk and financial markets: Insights from pandemic and military crisis periods

AK Banerjee et al. - Int. Rev. Econ. & Finance, 2024
XLRI、比尔肯特大学

![](https://fastly.jsdelivr.net/gh/bucketio/img4@main/2024/12/14/1734213725892-1873a49d-047e-4dbe-930d-4de62eaba312.png)

**结果 - 主要发现**
地缘政治风险放大金融市场波动与联动，军事冲突期更甚。

- 债券传递风险，黄金吸收风险。
- 指导政策与投资者风险管理。

---

#### Cross-quantile risk assessment: The interplay of crude oil, AI, clean tech, and other markets

M Gubareva et al. - Energy Economics, 2024
里斯本大学、BRAC大学

**结果 - 主要发现**
广义分位数对分位数方法揭示原油、AI、清洁科技与传统市场间风险传递。

- 为市场相互依赖性提供深入分析。
- 对政策与投资决策有启示。

---

#### Strategic Bonding Curves in Automated Market Makers

R Cartea et al. - SSRN, 2024
牛津大学

**结果 - 主要发现**
战略Bonding曲线改善AMM效率、稳定性与流动性。

- 理论与实证显示更可预测与稳定的交易环境。
- 为现代金融系统提供新思路。

---

#### Price divergence in bitcoin market

G Chu et al. - Rev. Quant. Finance & Accounting, 2024
南开大学、伯明翰商学院

**结果 - 主要发现**
国家分割、文化因素与交易所风险导致比特币价格差异，为套利提供机会。

- 链上成本与交易活动增加价格分歧。
- 更高区块链安全与用户采用度减少分歧。

---

#### Automated Market Making: the case of Pegged Assets

P Bergault et al. - arXiv:2411.08145, 2024
巴黎索邦、巴歇利耶研究所、巴黎多菲纳

**结果 - 主要发现**
利用多级嵌套OU过程为挂钩加密资产构建AMM模型，提高风险管理与流动性。

- USDC/USDT与wstETH/WETH数据验证模型高效性。
- 改善挂钩资产市场报价与流动性。

---
