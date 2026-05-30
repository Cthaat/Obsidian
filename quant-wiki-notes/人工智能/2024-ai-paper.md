---
title: "2024年AI量化论文优选"
category: "AI+量化"
tags: [AI+量化, 量化, 交易, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

# 2024年AI量化论文优选

本篇汇总收录了共计 **41 篇**（精选及拓展阅读）定量金融领域的**前沿研究成果**。这些论文涵盖了从股票、外汇、商品、固定收益与信用市场到投资组合优化、市场预测、衍生品建模、宏观经济与地缘政治风险，以及加密货币与 DeFi 等多元主题。尤其值得关注的是，越来越多的工作正将人工智能（AI）与大型语言模型（LLMs）引入金融分析与交易中，不仅提升预测与评估的精准度和效率，还为策略制定、投资决策与风险管理提供了全新思路。

## 目录

- 人工智能与大型语言模型在金融与交易领域的应用

  1. 基于大型语言模型的核心盈利测度扩展
  2. 利用自动编码器实现利率曲线的风险中性建模
  3. 大型语言模型在金融与投资管理中的应用与基准测试
  4. 利用“小波骑乘”方法发现新型金融价格跳跃类别
  5. 建模新闻交互与影响来预测金融市场
  6. 利用生成式AI获取经济洞察
  7. 将机器学习纳入Markowitz投资组合选择范式
  8. 多任务微调的“调酒效应”：以金融为案例研究
  9. 基于时空扩散模型进行缺失与实时金融数据推断
  10. “模拟与优化”：双层抵押贷款模拟器设计新型援助产品
  11. 减少歧视性偏差并可解释的XGBoost二分类框架

**投资组合策略与市场预测新进展**

  12. 针对不平衡面板数据的条件均值与协方差联合估计
  13. 利用 regimes 切换信号的动态因子配置
  14. 排名空间统计套利
  15. 投资组合选择中的均值-方差与均值-ETL优化更新
  16. 从金融分析师网络中提取阿尔法
  17. 在高风险水平和风险价格下预测股票溢价
  18. 基于全时域神经网络实现动态投资组合优化

**电子金融市场与限价订单簿(LOB)**

  19. 利用线性策略应对非线性价格影响
  20. 没有过小的最小价格变动：建模小Tick限价订单簿的通用方法
  21. 利用上下文信息进行信贷市场的多任务动态定价
  22. Maker-Taker（做市-接受）限价单补贴是否改善市场结果？
  23. 在决定性时间变流动性下的最优执行：适定性与价格操纵问题
  24. 稀疏订单簿的模拟与分析：在日内电力市场中的应用
  25. 流动性对金融市场“假报价”(Spoofing)可行性的影响
  26. 库存、做市与OTC市场流动性

**金融衍生品建模与波动率前沿**

  27. 考虑溢出效应的已实现波动率预测：图神经网络视角
  28. 利用二阶优化的快速深度对冲
  29. 基于图信号处理的全球股市波动率预测
  30. 借助永久衍生品对冲：三叉树期权定价与隐含参数曲面分析
  31. 基于Log Heston模型的月度平均VIX建模
  32. GARCH辅助神经网络用于金融市场波动率预测

**金融市场与宏观经济学新趋势**

  33. 推动中国信用债券市场流动性的因素
  34. 人工智能与大数据持仓：央行的新机遇
  35. 基于Brownian内核的GMM估计及收入不平等度量
  36. 驯服维度诅咒：利用深度学习的定量经济学
  37. 负均值产出缺口与统计滤波器的对称性偏差
  38. 货币市场的风格化事实：对欧元区数据的实证分析
  39. 在监管约束下的货币创造极简模型
  40. 竞争能否提高因子投资的利润？
  41. 利用动态图神经网络条件预测追缴保证金
  42. 面向价值-at-风险的时间序列基础模型
  43. 银行业模型验证实践：结构化方法

**去中心化金融(DeFi)前沿**

  44. 去中心化交易所的流动性驱动因素：来自Uniswap协议的证据
  45. AgileRate：为DeFi借贷市场带来适应性与稳健性

**时间序列预测**

  46. XForecast：为时间序列预测的自然语言解释评估
  47. 用在线保序推断实现多步时间序列预测的区间估计

**精选之外的前沿研究**
  48. 跨越边界：超出精选名单之外的研究

## 基于大型语言模型的核心盈利测度扩展

**论文信息：**
M Shaffer, CCY Wang, SSRN, 2024
University of Southern California, Harvard Business School
[原文链接](https://papers.ssrn.com)

**研究结果与关键发现**

本研究评估大型语言模型（LLMs）在通过10-K披露文件测量企业核心盈利方面的有效性，发现相较传统指标有显著改进。

- 当使用结构化“序列式”提示时，LLM生成的核心盈利指标在预测未来平均收益上优于GAAP净收益及其它常用指标。
- 与无结构“基线”方法不同，序列式方法能准确区分非经常性与经常性收益要素，提高预测有效性并减少与其他财务概念混淆。
- 基于LLM的核心盈利测度在预测长期净收益方面具备较高预测能力，并与未来市场估值强相关，有望大幅降低金融信息分析成本。

图2展示了GAAP净收益与两种LLM核心盈利估计值的分布直方图（均为每股值）。

- Lazy Analyst核心盈利/股：使用“Lazy Analyst”LLM提示
- Sequential Prompt核心盈利/股：序列式提示方法估计的核心盈利
- GAAP收益(每股净收益)

## 利用自动编码器实现利率曲线的风险中性建模

**论文信息：**
A Lyashenko, F Mercurio, A Sokol, SSRN 4967989, 2024
Quantitative Risk Management, Bloomberg, CompatibL
[原文链接](https://papers.ssrn.com)

**研究结果与关键发现**

该研究利用自动编码器(AE)在风险中性框架下对收益率曲线进行建模，既保留历史结构又保证无套利动态。

- 自动编码器为收益率曲线提供低维表征，实现历史一致性和市场价格高效校准。
- 研究提出一种通过凸性调整偏离AE流形的方法，确保远期利率曲线无套利演化。
- 数值结果在多货币利率互换数据中表现优异，提高曲线表示的精确度与对冲稳定性。

图1：展示静态无套利轨迹（蓝色）及生成流形环MXY在 δ=0.1,0.2,0.3 三种选择下的情况。

## 大型语言模型在金融与投资管理中的应用与基准测试

**作者：**
Kong Y, Nie Y, Dong X, Mulvey JM, Poor HV, Wen Q, Zohren S
（牛津大学、普林斯顿大学、Squirrel Ai）

**研究结果与关键发现**

- 基于LLM的多代理系统通过协作式专用代理和自反性推理框架，提升自动化交易、企业战略规划和市场情绪分析等任务的能力。
- 引入诸如FLUE、PIXIU等综合基准，为评估LLM 在金融自然语言处理任务（如金融预测、命名实体识别、情绪分析）建立稳健标准。
- 语言特定基准强调在不同语言环境中定制评估，以提高金融LLM 在全球市场中的适应性和有效性，并同时应对数据隐私和计算成本的挑战。

该论文强调LLM 在交易、企业规划、金融情绪分析方面的转型性应用及其评估基准的重要性。

**(第 10/65 页)**

---

## 利用“小波骑乘”方法发现新型金融价格跳跃类别

**作者：**
C Aubrun, R Morel, M Benzaquen, JP Bouchaud, 2024
(CNRS, Capital Fund Management, École Polytechnique, ENS)

**研究结果与关键发现**

本研究提出一种新型无监督分类方法，利用多尺度小波表示区分不同类型的金融价格跳跃和共跳跃，并由此获得有关其内生或外生性质的新见解。

- 波动率的时间不对称性是区分内生与外生价格跳跃的主要特征：内生跳跃更对称，而外生跳跃在跳跃后期体现更强的波动率。
- 本研究发现具有本地均值回复和趋势对齐特征的新型价格跳跃类别（如“均值回归型”和“趋势对齐型”跳跃）。
- 分析表明，多数大规模共跳跃事件由内生传染机制驱动，而非源于外生新闻，强调市场动态的内在互联与反身性。

附图显示295只美国股票在8年期间的共跳跃分布。横轴为日期，纵轴为发生跳跃的时间，每个圆点代表在1分钟间隔内发生的共跳跃数量和规模，较大、颜色更暖的圆点代表更多股票同时跳跃。研究显示2019年10月附近的共跳跃事件集中，突出市场活动和传染效应的高峰期。

## 建模新闻交互与影响来预测金融市场

**作者：**
M Wang, SB Cohen, T Ma - arXiv:2410.10614 (2024)
The University of Edinburgh

**研究结果与关键发现**

FININ模型通过融合新闻交互与市场数据在市场预测中表现优于现有方法。

- FININ提升S&P 500和NASDAQ 100的日均夏普比率分别达0.429和0.341，证明整合新闻与市场数据的有效性。
- 研究揭示新闻对市场定价有延迟效应、新闻存在长记忆效应、单纯情绪分析的局限性以及综合新闻分析的重要性。
- 利用数据融合编码器与市场感知影响量化器，模型在长达15年、超过270万篇新闻文本数据上测试。

图2展示FININ模型，包括数据融合编码器和市场感知影响量化器的结构，通过多层注意力、MLP等模块将市场与新闻特征整合并输出市场洞察。

## 利用生成式AI获取经济洞察

**作者：**
M Jha, J Qian, M Weber, B Yang - arXiv:2410.03897 (2024)
University of Chicago, Booth商学院, Georgia State University

**研究结果与关键发现**

研究引入了基于管理层预期的AI经济指数（AI Economy Score），可有效预测未来经济指标并优于现有测度。

- AI Economy Score能显著预测GDP增长、产出和就业等经济指标。
- 相较于调查预测等现有指标，该指数在长期预测与微观层面分析上更具优势。
- 利用向量自回归框架验证其长期可预测性与微观层面洞察，对政策制定者、研究人员与投资者具备实用价值。

图中展示2007Q1-2023Q1期间AI Economy Score与实际GDP增长以及SPF预测的对比，双坐标轴对比指数与GDP指标，揭示两者在时序上的动态关系。

## 将机器学习纳入Markowitz投资组合选择范式

**作者：**
M López de Prado, J Simonian, FA Fabozzi - Annals of Operations Research (2024)
Stevens Institute of Technology, Cornell University

**研究结果与关键发现**

研究利用深度Q网络(DQN)策略在多资产组合中显著优于传统方法，实现更高收益和更低风险。

- DQN策略比10种传统组合管理策略高出30%的利润，并在夏普比率、最大回撤方面表现更佳。
- 作者将DQN适应于多资产组合的离散动作空间，并结合CNN和对偶Q网络方法，提出一种离散化市场行为的方法。
- 在5只低相关性美股历史价格数据上测试，DQN策略在强化学习框架下持续优化未来累积回报，表现更优。

图5展示了在2017/01/05至2017/11/17测试期内，不同策略的累积回报曲线。DQN策略在测试期多数时间表现优于基准策略，尤其在中后期体现强大优势。

**(第 14/65 页)**

---

## 多任务微调的“调酒效应”提升LLM性能——以金融为例

**作者：**
M Brief, O Ovadia, G Shenderovitz, NB Yoash - arXiv:2024
Microsoft, Tel Aviv University

**研究结果与关键发现**

多任务微调显著提升LLM 在金融任务上的性能，使得较小模型通过任务整合超越更大模型。

- 研究显示，通过多任务微调，较小的Phi-3-Mini模型能在金融基准上优于更大的GPT-4-o模型。
- 实证验证“调酒效应”（cocktail effect），即在多关联任务上训练能协同提升模型性能。
- 引入通用指令数据作为正则化，利用数学数据提升数值推理能力，并通过对220个模型的系统探索验证数据集间的交互效应。

图1对比了GPT-4-o、Phi-3-Mini基线模型和最佳多任务微调Phi-3-Mini在金融任务（Twitter情感分析、主题分析、FinNerCLS、FPB任务、FinQA、ConvFinQA、Headline）上的表现，各任务条形图显示多任务微调显著提升成绩。

**(第 15/65 页)**

---

## 基于时空扩散模型的缺失与实时金融数据推断

**作者：**
Y Fang, R Liu, H Huang, P Zhao, Q Wu - ACM（2024）
City University of Hong Kong, Brunel University London

**研究结果与关键发现**

该研究提出了时空扩散模型(STDM)在金融数据插补中的创新方法，有效捕捉时空相关性并提升插补精度。

- 关键贡献包括特征专用投影、截面方向图卷积以及隐式采样器，既降低计算内存占用又保持高精度。
- 在OSAP数据集上的表现优于现有方法，并通过消融实验和因子投资组合构建验证模型有效性。
- 强调捕捉空间与时间依赖性对金融数据插补和实时分析的重要性。

图1展示STDM的预测器架构，包括多重残差块和特征映射，通过特征专用投影、时间注意力和截面方向图卷积提取时空依赖。

**(第 16/65 页)**

---

## “模拟与优化”：双层抵押贷款模拟器设计新型援助产品

**作者：**
L Ardon, BP Evans, D Garg, AL Narayanan - arXiv:2024
J.P. Morgan AI Research, University of Sydney

**研究结果与关键发现**

研究开发了一种创新的双层仿真方法，用于优化抵押贷款援助产品，增强家庭对金融冲击的抵御能力，并协助政策制定者。

- 作者扩展了基于主体的模型，实现反事实分析和基于产品条件的政策学习，提出通用参数化金融产品配置方法。
- 方法论包含用于家庭行为模拟的内层与产品设计优化的外层，并利用人口统计数据校准。
- 自适应仿真可识别有利配置，降低违约率，提升社会福利，为政策制定与金融机构提供可扩展、低成本工具。

图1显示了该双层优化方法结构：外层产品设计和内层模拟。内层在给定外层决策下优化家庭策略与产品分配参数，形成自适应闭环。

**(第 17/65 页)**

---

## 减少歧视性偏差且可解释的XGBoost二分类框架

**作者：**
A Pangia, A Sudjianto, A Zhang, T Khan - arXiv:2410.19067 (2024)
Wells Fargo, University of North Carolina at Charlotte

**研究结果与关键发现**

LDA-XGB1框架将公平性约束融入XGBoost，为金融信贷模型在平衡准确性与公平性方面提供新方法。

- LDA-XGB1将公平性约束和单调性纳入XGBoost，与传统公平信贷模型相比减少对受保护群体的偏见并保持可解释性。
- 作者提出一种双目标优化方法，利用分箱和信息值（IV），引入“较少歧视性备选项”（Less Discriminatory Alternative）和“公平信息值”（FIV），以降低差异影响。
- 在模拟和真实数据上测试，LDA-XGB1在公平性与准确性之间实现权衡，满足监管要求，为金融机构提供有力工具。

附图为单调XGB1模型中的特征重要性条形图，其中Mortgage特征在Inquiry、Balance、Utilization、Amount Past Due、Delinquency、Open Trade中占主导地位。

**(第 18/65 页)**

---

## 针对不平衡面板的条件均值与协方差联合估计

**作者：**
D Filipovic, P Schneider - arXiv:2410.21858 (2024)
EPFL, Swiss Finance Institute

**研究结果与关键发现**

研究提出非参数模型，用于同时估计不平衡面板数据的条件均值与协方差，在实证资产定价中优于传统模型。

- 模型具备一致性与有限样本保证，同时保持协方差矩阵的正定性与对称性。
- 在1962-2021年美国股票数据上，该方法显示出显著的样本外夏普比率提升，相较于常量协方差模型有显著改进。
- 使用凸优化、低秩近似和Nystrom方法，实现大规模实证分析的计算效率。

图中四个折线图比较使用余弦与高斯核的样本外预测R²表现。在m=5、10、20、40的不同取值下，对1962至2021年不平衡美股超额收益数据分析，阴影区域标注重大市场崩盘时期。

**(第 19/65 页)**

---

## 利用regime切换信号的动态因子配置

**作者：**
Y Shu, JM Mulvey - arXiv:2410.14841 (2024)
Princeton University

**研究结果与关键发现**

利用稀疏跳模型（Sparse Jump Model）识别市场regime，可改善因子配置绩效，为动态资产配置提供有力方法。

- 利用稀疏跳模型识别市场状态，实现所有因子正夏普比率且因子间相关性低。
- 将regime推断纳入Black-Litterman框架，使动态配置策略在信息比率和最大回撤方面优于静态基准。
- 在七个美国股权因子上进行测试，利用历史数据和市场环境特征提出新颖的因子regime分析方法，有别于传统因子择时策略。

图中展示了2012至2024年间价值因子（Value Factor）的累计超额收益曲线，使用Sparse Jump模型识别牛市（绿）与熊市（红）状态，蓝线为累计收益表现。

**(第 20/65 页)**

---

## 排名空间的统计套利

**作者：**
YF Li, G Papanicolaou - arXiv:2410.06568 (2024)
Stanford University

**研究结果与关键发现**

在排名空间(rank space)应用神经网络从事统计套利，比传统方法显著提高收益率与夏普比率。

- 提出在排名空间进行统计套利的框架，以日内再平衡与神经网络优化实现2007至2022年平均35.68%的年收益率，夏普比率3.28。
- 相较传统的名称空间(name space)，排名空间由单一因子驱动的稳定市场结构并具有更强的均值回复特性。
- 利用美国股票数据、主成分分析(PCA)分解与神经网络优化投资组合，与参数模型相比，排名空间中的神经网络策略表现更佳。

图中多个子图比较名称空间与排名空间的市场结构差异，如市场资本化占比、相关矩阵主特征值、特征值谱的经验概率分布等。

**(第 21/65 页)**

---

## 均值-方差与均值-ETL优化在投资组合选择中的更新研究

**作者：**
BP Shao, JB Guerard Jr, G Xu - Annals of Operations Research (2024)
Tudor Investment Corporation

**研究结果与关键发现**

利用分析师预测的综合变量进行稳健回归及优化组合，可在考虑交易成本后仍实现显著活跃收益。

- 将分析师预测、修正及其方向整合为复合变量并纳入稳健回归模型，在投资组合中实现显著的活跃回报。
- 均值-方差与均值-ETL优化在统计上显著产生活跃收益，通过数据挖掘修正检验依旧可靠。
- 使用时间序列模型与多元正态厚尾分布创新，以及Beaton-Tukey加权回归技术应对离群值，在实际场景下提高回报潜力。

该论文更新了投资组合选择中MV与ETL优化应用的研究结果，强调稳健回归模型的有效性。

**(第 22/65 页)**

---

## 从金融分析师网络中提取阿尔法

**作者：**
D Gorduza, Y Kong, X Dong, S Zohren - arXiv:2410.20597 (2024)
University of Oxford

**研究结果与关键发现**

将图注意力网络(GAT)应用于分析师覆盖网络可显著提升交易策略效果，捕捉复杂公司间关系。

- 利用GAT模型对分析师覆盖网络建模，显著提升交易策略年化收益率(29.44%)与夏普比率(4.06)，优于传统方法。
- GAT捕捉公司间复杂非线性关系，通过同时分析公司特征与网络结构，预测股票表现并制定灵活自适应的交易策略。
- 数据范围2006-2022年，使用股票价格与分析师估计构建网络，边代表分析师共同覆盖的股票，实现图机器学习在金融市场应用的潜力。

图中展示了GAT交易模型管线，从股票价格、特征矩阵、分析师覆盖和邻接矩阵出发，经GAT处理后输出未来回报预测。

**(第 23/65 页)**

---

## 使用高阈值风险水平与风险价格预测股票溢价

**作者：**
N Bansal, C Stivers - Financial Management (2024)
University of Louisville

**研究结果与关键发现**

研究表明利用VIX和情绪指数可有效预测美国股票溢价，并在不同市场环境下展现出稳健预测能力。

- 当市场情绪高（低风险时期）时，股票溢价下降；当VIX超过80%-85%分位数时（高风险时期），溢价大幅上升。
- 在6个月和12个月的预测视角下，预测调整后R²分别达19%和29%，表现出跨时段与市场条件下的稳健预测力。
- 利用1990-2023年数据进行样本内外检验，并辅以控制变量，对市场动态的精细理解可提高金融预测与风险评估的精准度。

本研究关注VIX与情绪对股权风险溢价的影响，当VIX处于高位时，市场应对风险的溢价明显上升，为投资者风险评估和政策制定提供参考。

**(第 24/65 页)**

---

## 基于全时域神经网络的动态投资组合优化

**作者：**
PM van Staden, PA Forsyth, Y Li - Applied Mathematical Finance (2024)
University of Waterloo

**研究结果与关键发现**

本研究提出一种无需动态规划的全时域( global-in-time )神经网络模型，用于动态投资组合优化，性能优于传统方法。

- 无需传统动态规划的神经网络模型，为复杂金融问题提供更灵活高效的优化方法。
- 引入新颖方法与术语，利用高级神经网络结构与市场模拟展示神经网络可处理投资组合优化中的复杂性。
- 模型在模拟结果中表现优于传统方案，为金融优化问题提供新的研究方向。

该论文为动态投资组合优化提供了一种创新的神经网络方法，避免动态规划的限制，开辟了金融优化的新路径。

**(第 25/65 页)**

---

## 利用线性策略应对非线性价格影响

**作者：**
Brokmann X, Itkin D, Muhle-Karbe J, Schmidt P
Mathematical Finance (2024)
Qube Research and Technologies, Imperial College London, LSE

**研究结果与关键发现**

该研究表明，对于非线性价格冲击，利用为二次成本优化的线性交易策略即可接近最优性能，通过调整有效成本参数实现。

- 针对非线性价格冲击优化的线性策略，性能损失低于2%，适用于广泛风险水平。
- 将有效二次成本参数适配价格冲击的凹性，使线性策略表现接近复杂数值算法，但计算负担更低。
- 方法无需高级数值求解，即可在具有非线性冲击的市场中取得接近最佳绩效，为现实交易提供实用方法。

图示中展示了年化盈亏(P&L)曲线，与高度复杂的Kolm-Ritter Viterbi算法相比，经过优化的线性策略曲线十分接近，可见调整后线性策略的有效性。

**(第 26/65 页)**

---

## 没有过小的最小价格变动：通用建模小Tick限价订单簿方法

**作者：**
K Jain, JF Muzy, J Kochems, E Bacry - arXiv:2410.08744 (2024)
University College London, University of Oxford

**研究结果与关键发现**

研究提出通用 Hawkes Process 模型模拟不同tick规模下的限价订单簿动态，揭示大、中、小tick股票间显著特征差异。

- 利用高频LOB数据对15只股票分类（大、中、小tick），分析买卖价差、价格变动及流动性分布的关键特征。
- 提出通用Hawkes过程模型，可模拟小tick股票的订单薄动态，并通过在不同资产间的模拟验证其普适性。
- 研究为应对小tick股票建模的挑战提供新方法，为未来对LOB动力学研究指明方向。

图示为平均买卖价差与相对tick大小的对数坐标图，不同股票（大tick和中小tick）表现出不同的斜率与线性关系。

**(第 27/65 页)**

---

## 利用上下文信息实现信贷市场多任务动态定价

**作者：**
A Javanmard, J Ji, R Xu - arXiv:2410.14839 (2024)
NYU, USC

**研究结果与关键发现**

TSMT算法通过利用证券间结构相似性提升金融定价准确度，优于单独或合并定价策略。

- 在分段实验设置中，TSMT算法利用证券间相似性在竞争对手定价的线性上下文模型中获得优越表现。
- 使用最大似然法进行参数估计，可有效应对数据稀疏与删失反馈问题。
- 在合成与真实数据（包括美国公司债券定价）上实验，TSMT在不同证券与异构条件下能适应相似结构，实现更低遗憾度。

图示中展示了在不同问题配置下的TSMT策略相对于个体学习与合并策略的遗憾度对比，TSMT在适度相似性条件下表现出色。

**(第 28/65 页)**

---

## Maker-Taker限价单补贴是否改善市场结果？准自然实验证据

**作者：**
Y Lin, PL Swan, FHB Harris - Journal of Banking & Finance (2024)
UNSW, Wake Forest University

**研究结果与关键发现**

研究显示Maker-Taker补贴改善市场效率却增加交易成本，当补贴移除时，市场质量恶化，影响市场行为。

- Maker-Taker补贴提高市场深度与效率，但也延长限价队列，增加交易成本。
- NASDAQ费用试点显示，移除补贴后市场份额下降，市场质量变差，反驳了“抵消论”（washout theory）。
- 通过整合监管框架、强调未计费用的原始价格数据，利用专有NASDAQ数据和差分法分析，揭示费用结构对市场微观结构的影响。

图B显示NASDAQ在5秒间隔内的价格冲击对照图，并标注在补贴减少与恢复时对价格影响的时间序列对比。

**(第 29/65 页)**

---

## 在决定性时间变流动性下的最优执行：适定性与价格操纵问题

**作者：**
G Palmari, F Lillo, Z Eisler - arXiv:2410.04867 (2024)
Imperial College London, Bologna大学

**研究结果与关键发现**

研究表明在时间变流动性条件下的最优执行问题存在适定解，并在一定条件下避免价格操纵。

- 定义强弱适定性条件，利用B矩阵理论确保非负交易成本。
- 提出新条件避免由交易引发的价格操纵，证明Almgren-Chriss模型在时间依赖影响下的鲁棒性。
- 利用变分法和数值模拟验证理论结果，强调控制流动性变化速率对保持适定性的重要性，为实际交易策略提供参考。

图1展示了微软股票在2021年6月的日内临时影响与永久影响动力学，以及2021年6月10日的永久影响变化，提供实证背景。

**(第 30/65 页)**

---

## 模拟与分析稀疏订单簿：在日内电力市场中的应用

**作者：**
P Bergault, E Cognéville - arXiv:2410.06839 (2024)
Université Paris Dauphine-PSL, EDF R&D

**研究结果与关键发现**

该研究用非齐次泊松过程模型模拟低流动性市场的订单流，为LOB动态提供更真实的刻画。

- 应用于欧洲日内电力市场，分析EPEX Spot数据（德国、法国），重点关注小时交割周期。
- 模拟显示订单到达与撤单的零星特性，市场接近交割时点利差增大、价格波动加剧，与实证行为一致。
- 尽管无法完全捕捉极端事件，模型为低流动性市场的订单簿建模提供参考基础。

图1展示2021年1月7日某交易日不同产品的日内中价(mid-price)演变曲线，图2则展示2021年1月产品下不同时间对市场交互强度的均值变化。

**(第 31/65 页)**

---

## 流动性对金融市场“假报价”可行性的影响

**作者：**
A Gu, Y Wang, C Mascioli, M Chakraborty, R Savani - 2024
University of Michigan, University of Liverpool

**研究结果与关键发现**

高市场流动性降低“假报价”（spoofing）的有效性，表明维持充足流动性有助于抵御市场操纵。

- 利用强化学习和参数优化开发高级spoofing策略，在代理模型中比现有方法更高盈利和冲击力。
- 发现两种spoofing行为模式：高流动性市场下低利高频成交需多次进场；低流动性市场下高利低频策略反而有效。
- 提示监管机构通过提高市场流动性可自然减弱spoofing行为。

图2展示了spoofing对策略方与背景交易者（HBL、ZI）的盈余影响对比图，不同市场配置（A1,A2,A3,B1,B2,B3,C1,C2,C3）下，基准与R-Learned、Tuned策略比较盈余情况。

**(第 32/65 页)**

---

## OTC市场中的库存、做市与流动性

**作者：**
A Cohen, M Kargar, B Lester, PO Weill - Journal of Economic Theory (2024)
Federal Reserve Bank of Philadelphia, UCLA

**研究结果与关键发现**

研究通过搜索理论框架模型化做市商的库存成本与监管影响，探究OTC市场的流动性与福利影响。

- 做市商在OTC市场需持有库存以促进交易，从而影响买卖价差、成交量等流动性指标。
- 利用校准模型分析后危机时代的监管及其对经销商行为与市场福利的影响，强调库存成本对流动性的关键作用。
- 研究假设经销商只能卖出所拥有的资产，显示监管提高库存成本减少流动性与福利。

图示展示了目标资产持有量q*()在有无库存限制(CKLW与LR)条件下的比较。

**(第 33/65 页)**

---

## 考虑溢出效应的已实现波动率预测：图神经网络视角

**作者：**
C Zhang, X Pu, M Cucuringu, X Dong - International Journal of Forecasting (2024)
Oxford-Man Institute, Alan Turing Institute, HKUST(GZ)

**研究结果与关键发现**

通过图神经网络(GNN)预测多元已实现波动率，将溢出效应纳入模型，显著提升预测精度。

- 考虑多跳邻居的溢出效应未必 consistently 改善预测精度，直接邻居信息已足够提高性能。
- 基于GNN的非线性溢出效应建模在短期（周内）波动率预测方面表现更优。
- 使用类似似然的损失函数训练，改善异方差性处理能力，相比传统HAR模型表现更佳。

图示以IBM为例，展示波动率通过网络结构向其他股票扩散的路径（0跳、1跳、2跳邻居），强调直接与多级传播的影响比较。

**(第 34/65 页)**

---

## 利用二阶优化加速深度对冲

**作者：**
K Mueller, A Akkari, L Gonon, B Wood - arXiv:2410.22568 (2024)
Imperial College London, J.P. Morgan

**研究结果与关键发现**

新二阶优化方法(KFAC)为深度对冲训练加速75%，在高曲率损失区域更快收敛并提升对冲性能。

- 使用KFAC与收缩型阻尼处理，实现二阶优化方案，加速神经网络训练，较Adam减少75%优化步骤。
- 引入动态演化的对冲操作空间，在随机波动模型下对棘轮(cliquet)期权对冲进行验证。
- 实验表明期权对冲至关重要，二阶优化方法在高曲率损失区域表现更佳，快速收敛并改善对冲绩效。

图1展示了飘动网格(Floating grid)中隐含波动率曲面的随机性及可用看涨/看跌期权位置的示意。

**(第 35/65 页)**

---

## 基于图信号处理的全球股市波动率预测

**作者：**
Z Chi, J Gao, C Wang - arXiv:2410.22706 (2024)
The University of Sydney

**研究结果与关键发现**

利用图信号处理(GSP)和异质自回归(HAR)模型的融合（GSPHAR），通过图傅里叶变换和卷积滤波提高多市场波动率预测。

- 基于光谱图理论和磁性拉普拉斯，构建全球24个股指的波动溢出网络，捕捉复杂市场间关联。
- GSPHAR引入可学习的卷积滤波器，更动态地聚合过去信息，展现更灵活的衰减模式。
- 相比传统HAR模型，GSPHAR在短、中、长期预测任务中均有更好表现，强调方向性和非线性溢出效应的重要性。

图示模型架构展示从输入多元RV时间序列，到磁性拉普拉斯分解、图傅里叶变换、卷积过滤及最终预测输出的流程。

**(第 36/65 页)**

---

## 通过永久衍生品对冲：三叉树期权定价与隐含参数曲面分析

**作者：**
J Gnawali, WB Lindquist, ST Rachev - arXiv:2410.04748 (2024)
Texas Tech University

**研究结果与关键发现**

研究提出一套使用三叉树模型与多资产组合分析的定价方法，可同时估计风险中性和现实世界参数。

- 利用可复制组合推出风险中性动态，通过假设检验标定真实世界参数。
- 引入新方法标定价格变动概率并计算隐含参数曲面，包括波动率、均值、无风险利率及概率分布参数。
- 在分析科技巨头股票数据中，研究构建了三叉树模型并实证出市场对未来股价表现的预期，填补风险中性与现实世界参数间的差距。

图1展示了基本的三叉树结构与时间步k、级别i的索引示例。

**(第 37/65 页)**

---

## 基于Log Heston模型的月度平均VIX建模

**作者：**
J Park, A Sarantsev - arXiv:2410.22471 (2024)
University of Michigan, University of Nevada, Reno

**研究结果与关键发现**

通过将VIX取对数并应用Heston模型(对数Heston模型)，将月度股指收益标准化后更接近高斯独立同分布，提高对波动率与收益率的建模精度。

- 将月度股指收益Rt标准化为Rt/VIXt后，其分布更接近高斯独立同分布，减小偏度与峰度。
- 对数Heston模型对log(VIXt)进行AR(1)建模，相比原Heston模型拟合更好。
- 数据覆盖1986至2024年，残差呈非高斯分布，方差-伽马分布对创新的拟合更佳。

图中展示了1986年至2024年6月的VIX时间序列与标准化回报率的对比图，VIX在10至60区间波动，小价格回报率围绕零上下浮动。

**(第 38/65 页)**

---

## GARCH辅助神经网络预测金融市场波动率

**作者：**
Z Xu, J Liechty, S Benthall, N Skar-Gislinge - arXiv:2024
Carnegie Mellon University, NYU

**研究结果与关键发现**

GARCH-Informed Neural Networks (GINN)在波动率预测中融合GARCH模式与LSTM的优势，精度与泛化性优于传统模型。

- 将GARCH经验规律融入LSTM神经网络，平衡模型精度与泛化能力。
- GINN及其变体GINN-0在全球多市场指数数据上的预测表现超过传统GARCH与GAS模型。
- 通过在损失函数中加入GARCH预测作为正则项，GINN模型同时捕捉短期与长期市场特征，减少过拟合。

图4展示GINN模型的方差预测流程，包含Log Return、AR+GARCH、GINN与真实方差间的关系，用MSE衡量GINN与GARCH预测差异。

**(第 39/65 页)**

---

## 推动中国信用债券市场流动性的因素

**作者：**
J Mo, MG Subrahmanyam - The Journal of Finance and Data Science (2024)
NYU, NYU Shanghai

**研究结果与关键发现**

对2010-2019年中国信用债市场分析，发现流动性效应在不同市场与品种间存在显著差异，并受政策干预与宏观经济条件影响。

- 利用主成分分析衡量流动性，发现交易所市场流动性效应强于其他市场。
- 债券风险与宏观经济渠道对流动性影响显著，而公司信息渠道影响相对较弱。
- 围绕政策冲击的反事实分析显示流动性水平和定价方式的变化，凸显市场分割、监管变化及宏观条件对流动性的影响。

图示展示四类信用债券（企业债、中票、交易所企业债、公司债）的月度聚合流动性水平（以5个非流动性代理的第一主成分表示）。

**(第 40/65 页)**

---

## 人工智能与大规模持仓数据：央行机遇

**作者：**
X Gabaix, RSJ Koijen, R Richmond, M Yogo - 2024 - bis.org
Harvard, NYU Stern

**研究结果与关键发现**

利用资产需求系统结合AI与大持仓数据可为央行提供更深入的金融稳定与政策干预洞察。

- 引入AI驱动的embedding与大规模持仓数据测度资产与投资者相似性，提高资产需求系统的精度。
- 有助央行理解金融传染、资产价格波动及非常规货币政策影响，并优化气候压力测试、外汇储备管理。
- 利用先进计量工具和高质量组合数据，研究强调投资者需求的非弹性特征，挑战传统金融模型。

该BIS论文探讨AI与大数据在央行政策、资产定价与金融稳定中的作用。

**(第 41/65 页)**

---

## 利用Brownian核的GMM估计及收入不平等测度

**作者：**
JS Cho, PCB Phillips - 2024
Yale University, Yonsei University

**研究结果与关键发现**

本研究将Brownian运动与Brownian桥核引入无穷维GMM估计，用于收入不平等分析，提出新U检验。

- 引入BM-GMM与BB-GMM方法处理无穷维GMM估计问题，并提出U检验补充传统J检验。
- 利用连续工作历史样本数据库分析表明劳动力收入不平等在职业早期达到峰值，建议针对早期干预政策以减少不平等。
- 方法拓展对高维矩条件的处理能力，强调整体计算稳健性与分布假设下的稳健推断。

该研究为度量收入不平等提供新型计量方法，并展示其政策意义。

**(第 42/65 页)**

---

## 驯服维度诅咒：利用深度学习的定量经济学

**作者：**
J Fernández-Villaverde, G Nuño, J Perla - 2024 - nber.org

**研究结果与关键发现**

深度神经网络可克服高维动态均衡模型求解中的维度诅咒，提高经济学计算效率。

- 深度学习方法在求解高维随机新古典增长模型等复杂动态均衡模型中优于传统数值方法。
- 神经网络从经济学已有方法中推广出新的函数近似形式，为宏观、金融、博弈论应用提供新视角。
- 利用模拟数据训练神经网络逼近政策函数和均衡条件，为解决过去难以处理的高维经济问题提供可行路径。

该研究显示深度神经网络能改变定量经济学研究范式，拓宽研究适用范围。

**(第 43/65 页)**

---

## 负均值产出缺口与统计滤波器的对称性偏差

**作者：**
S Aiyar, S Voigts - IMF Economic Review (2024)
IMF, Johns Hopkins University

**研究结果与关键发现**

对称性偏差导致标准滤波器在深度衰退期低估潜在产出，令政策反应偏弱并增大产出损失。

- 标准统计滤波器假定产出缺口均值为零，当深度衰退时此假设偏差导致潜在产出被低估。
- 使用新凯恩斯模型模拟，发现工资下行刚性加剧衰退期就业下降，对称性偏差使决策者过早收紧政策。
- 在最深25%衰退期中，对称性偏差导致产出损失额外增加三分之一，强调更准确的产出缺口测算对反周期政策的重要性。

该研究为改进潜在产出估计和避免政策失误提供参考。

**(第 44/65 页)**

---

## 货币市场的风格化事实：对欧元区数据的实证分析

**作者：**
VL Coz, N Allaire, M Benzaquen, D Challet - arXiv:2024
Ecole Polytechnique, European Central Bank

**研究结果与关键发现**

LCR（流动性覆盖率）监管推动“永续回购”（evergreen repos）增加，使欧元区银行间网络更稠密、稳定，并更偏向有担保借贷。

- LCR监管后永续式回购协议大幅增加，反映欧元区货币市场从无担保向有担保交易转型。
- 底层数据表明担保品循环使用率约为1，与文献一致，且欧元区银行间网络比无担保市场更稠密对称。
- 使用ECB的MMSR数据分析47家大型欧元区银行的融资活动，说明永续回购在应对LCR限制中发挥关键作用。

图1展示从季度聚合的无担保与有担保货币市场交易量变化趋势，从历史数据到MMSR数据的对比。

**(第 45/65 页)**

---

## 在监管约束下的货币创造极简模型

**作者：**
VL Coz, M Benzaquen, D Challet - arXiv:2410.18145 (2024)
École Polytechnique, CentraleSupélec

**研究结果与关键发现**

利用主体模型研究银行在监管约束下的流动性管理，揭示不对称应对付款冲击导致货币市场中流动性过剩。

- 银行在面对付款冲击时采取不对称策略管理LCR，引发货币市场中永续回购增加。
- 随着抵押品稀缺度增加，抵押品再利用率提高；永续回购使银行满足流动性需要又不影响LCR。
- 模拟结果凸显抵押担保交易在维护金融稳定中的重要性，并为理解监管对货币市场动态的影响提供新视角。

图7展示了在不同存款流出率下的平均监管比例、抵押品再利用与网络密度变化。

**(第 46/65 页)**

---

## 竞争能否提高因子投资的利润？

**作者：**
V DeMiguel, A Martin-Utrera - Management Science (2024)
London Business School, Iowa State University

**研究结果与关键发现**

研究发现竞争会降低同一因子策略的利润，但若竞争者利用不同因子，多因子分散化有助提升利润。

- 多个投资者同时利用同一因子导致价格冲击与利润降低；而利用不同因子可通过交易分散化增加利润。
- 分散化可抵消因子竞争的负面影响，产生正外部性。
- 利用18个因子和共同基金持仓数据、博弈论模型与实证分析证明了竞争对因子收益的双重影响。

图示分别展示不同因子与投资规模下的总利润变化曲线，不同颜色线条表示多重投资者数量的影响。

**(第 47/65 页)**

---

## 利用动态图神经网络条件预测追缴保证金

**作者：**
M Citterio, M D’Errico, G Visentin - arXiv:2410.23275 (2024)
European Central Bank, ETH Zurich

**研究结果与关键发现**

新型DGNN架构可准确预测金融网络中高达21天的净变动保证金(NVM)需求，为系统性风险监测提供前瞻性工具。

- 将网络动力学纳入压力测试，通过构建基于隔夜指数互换的动态金融网络，拓展传统风险评估方法。
- 使用GC-LSTM模型提取时空模式，模拟数据训练DGNN模型，使其在压力测试场景下具备泛化和预测能力。
- 研究标志着从事后(ex-post)到事前(ex-ante)系统性风险评估的转变，有助中央银行与监管机构监测利率冲击下的市场反应。

图示对比1步与10步预测NVM的结果曲线，并与基准作比较，显示DGNN在较长期预测中仍保持较高精度。

**(第 48/65 页)**

---

## 面向VaR的时间序列基础模型

**作者：**
A Goel, P Pasricha, J Kanniainen - arXiv:2410.11773 (2024)
Tampere University, IIT Ropar

**研究结果与关键发现**

微调TimesFM（谷歌预训练时间序列基础模型）优于传统经济计量模型，为价值风险(VaR)估计提供数据驱动方案。

- 微调TimesFM在VaR预测方面超越GARCH、GAS等传统模型，并适用于多种置信水平。
- 研究表明，相较于纯经济计量方法，基础模型加微调的数据驱动方式更具灵活性与泛化性。
- 使用S&P 100指数19年每日回报数据，通过实际-预期比例与分位数评分等度量进行回测，支持转向数据驱动方法。

图中为不同模型在1%、2.5%、5%、10% VaR水平下，未拒绝零假设的资产数量对比，高者表示模型预期违约率与实际更一致。

**(第 49/65 页)**

---

## 银行业模型验证实践：结构化方法

**作者：**
A Sudjianto, A Zhang - arXiv:2410.13877 (2024)
Wells Fargo

**研究结果与关键发现**

综述模型验证在银行业的实施重点，包括概念健全性、结果分析与持续监测等环节，以确保模型合规与可靠性。

- 提供结构化的模型验证框架，强调概念合理性评估、成果分析和持续监测三大支柱。
- 回顾SR11-7/OCC11-12监管指导强调的模型风险管理，无新术语，但重申长期实践经验的重要性。
- 强调持续监测与评估对确保模型可信度和决策支持的重要性。

该研究对银行模型验证的重要性与实务操作提供了清晰结构化的指导。

**(第 50/65 页)**

---

## 去中心化交易所Uniswap的流动性驱动因素

**作者：**
BZ Zhu, D Liu, X Wan, G Liao, CC Moallemi - arXiv:2024
Columbia University, Uniswap Labs

**研究结果与关键发现**

研究发现影响Uniswap v3流动度的核心因素，包括gas费、代币回报及波动率，并引入新指标细化分析。

- 流动性集中度受gas价格、标的代币收益和波动性驱动；费收入与markout同时影响TVL与流动性集中度。
- 引入v2反事实价差指标，深入分析流动性集中度变化及影响因素。
- 竞争加剧与外部流动性来源导致流动性分散，影响Uniswap v3的市场深度。

研究为理解DeFi流动性动态、竞争格局以及价格机制提供数据驱动证据。

**(第 51/65 页)**

---

## AgileRate：为DeFi借贷市场带来适应性与稳健性

**作者：**
M Bastankhah, V Nadkarni, X Wang - arXiv:2024
UIUC, Princeton University

**研究结果与关键发现**

AgileRate动态模型通过自适应利率控制器（RLS算法）大幅提升借贷利用率与减低清算风险，优于静态模型。

- 引入自适应利率控制器并使用递归最小二乘（RLS）算法，提出新利率收敛和利用率稳定性的保证。
- 在Aave数据上验证AgileRate比静态协议表现更佳，在保持最优利用率与降低清算风险方面胜出。
- 方法具理论担保，抵御对手操纵，权衡适应性与稳健性，在动态市场条件下表现优良。

图中比较RLS控制器与Aave静态曲线在利用率随时间变化的表现，以及在有高转移噪声情况下的利用率误差，RLS始终保持稳健。

**(第 52/65 页)**

---

## XForecast：为时间序列预测的自然语言解释评估

**作者：**
T Aksu, C Liu, A Saha, S Tan, C Xiong - arXiv:2024
NUS, Salesforce Research

**研究结果与关键发现**

提出新的评价指标衡量时间序列预测的自然语言解释，发现数值推理能力比模型规模更重要。

- 引入直接与合成可模拟性两种新指标，以评估解释文本在预测模型产出与泛化到新数据时的帮助程度。
- 实验表明数值推理能力对解释质量至关重要，大模型尺寸并非决定因素。
- 通过多个数据集与模型的实验，这些指标与人类判断一致，可有效区分优劣解释。

图2展示两种指标：直接可模拟性与合成可模拟性，用以评估解释对预测的一致性与拓展性。

**(第 53/65 页)**

---

## 用在线保序推断实现多步时间序列预测的区间估计

**作者：**
X Wang, RJ Hyndman - arXiv:2410.13115 (2024)
Monash University

**研究结果与关键发现**

AcMCP方法通过考虑非平稳AR过程中多步预测误差的自相关性，为多步预测提供更有效的预测区间。

- 优化h步预测误差的结构，在非平稳自回归模型中，预测误差至多存在到滞后(h-1)的自相关。
- 引入AcMCP方法纳入这些自相关性，以无分布假设的方式获得长期覆盖保证。
- 在用电需求与餐饮消费支出预测中，AcMCP方法相比传统方法更具统计效率和可靠的覆盖率。

图3显示AR(2)模拟结果中，不同方法在各预测步长下的覆盖率与区间宽度的箱型图对比，AcMCP在目标覆盖率附近表现更稳定。

**(第 54/65 页)**

---

## 超出精选论文范围的前沿研究

以下为除本精选名单外的值得关注的论文列表，按主题、影响力、作者、发表与引用情况综合考虑。

**人工智能与LLM 在金融与交易中的应用**

1. GPT-Signal: Generative AI for Semi-automated Feature Engineering in the Alpha Research Process
2. Generative AI in Financial Reporting
3. Aligning LLMs with Human Instructions and Stock Market Feedback in Financial Sentiment Analysis
4. CustomizedFinGPT Search Agents Using Foundation Models
5. Large Language Models in Economics
6. The macroeconomic implications of the Gen-AI economy
7. What Role Does AI Play In Modern Financial Transactions?
8. Efficient Training of Neural Stochastic Differential Equations by Matching Finite Dimensional Distributions
9. Generation of synthetic financial time series by diffusion models
10. Financial Time Series Forecasting Based on Adversarial Training and Dynamic Weight Design
11. A scoping review of ChatGPT research in accounting and finance
12. Opportunities and Challenges of Generative-AI in Finance

**(第 55/65 页)**

---

## 前沿探索：精选之外的研究（续）

13. Multiple Objectives Escaping Bird Search Optimization and Its application in Stock Market Prediction Based on Transformer Model
14. FinTeamExperts: Role Specialized MOEs For Financial Analysis
15. Financemath: Knowledge-intensive math reasoning in finance domains
16. Deep Learning in Finance: A Survey of Applications and Techniques
17. Natural language processing in finance: A survey
18. FLAG: Financial Long Document Classification via AMR-based GNN
19. The Local Effects of Artificial Intelligence Labor Investments: Evidence from the Municipal Bond Market
20. Enhancing LLM Trading Performance with Fact-Subjectivity Aware Reasoning
21. The Role of Artificial Intelligence in Investment Decision-Making: Opportunities and Risks for Financial Institutions
22. From Facts to Insights: A Study on the Generation and Evaluation of Analytical Reports for Deciphering Earnings Calls
23. Temporal Relational Reasoning of Large Language Models for Detecting Stock Portfolio Crashes
24. GraphVAE: Unveiling Dynamic Stock Relationships with Variational Autoencoder-based Factor Modeling
25. Mapping Hong Kong’s Financial Ecosystem: A Network Analysis of the SFC’s Licensed Professionals and Institutions
26. FAMMA: A Benchmark for Financial Domain Multilingual Multimodal Question Answering

**(第 56/65 页)**

---

## 前沿探索：精选之外的研究（续）

27. Exploiting Risk-Aversion and Size-dependent fees in FX Trading with Fitted Natural Actor-Critic
28. Distilling Analysis from Generative Models for Investment Decisions
29. Large Legislative Models: Towards Efficient AI Policymaking in Economic Simulations
30. The effect of ESG divergence on the financial performance of Hong Kong-listed firms: an artificial neural network approach
31. A comparative analysis of SHAP, LIME, ANCHORS, and DICE for interpreting a dense neural network in Credit Card Fraud Detection
32. Hierarchical Reinforced Trader (HRT): A Bi-Level Approach for Optimizing Stock Selection and Execution
33. The Perks and Perils of Machine Learning in Business and Economic Research
34. Decrypting Corporate Speak: GPT-Assisted Measurement of Facts and Tones in Earnings Calls
35. TraderTalk: An LLM Behavioural ABM applied to Simulating Human Bilateral Trading Interactions
36. Enhancing Compliance And Kyc Processes Through Ai, Ocr, And Automation: A Costeffective- Approach

**投资组合策略与市场预测新进展**

37. Deep Learning Methods for S Shaped Utility Maximisation with a Random Reference Point

**(第 57/65 页)**

---

## 前沿探索：精选之外的研究（续）

38. Two-fund separation under hyperbolically distributed returns and concave utility function
39. Robust forward investment and consumption under drift and volatility uncertainties: A randomization approach
40. Clustering Digital Assets Using Path Signatures: Application to Portfolio Construction
41. Machine Learning for Real-Time Portfolio Rebalancing: A Novel Approach to Financial Optimization
42. Time evaluation of portfolio for asymmetrically informed traders
43. Conformal Predictive Portfolio Selection
44. Predicting the stock market prices using a machine learning-based framework during crisis periods
45. MFB: A Generalized Multimodal Fusion Approach for Bitcoin Price Prediction Using Time-Lagged Sentiment and Indicator Features
46. Kendall Correlation Coefficients for Portfolio Optimization
47. Delegated portfolio management with random default
48. Deep prediction on financial market sequence for enhancing economic policies
49. Economic Theory and Machine Learning Integration in Asset Pricing and Portfolio Optimization: A Bibliometric Analysis and Conceptual Framework
50. Generalized Distribution Prediction for Asset Returns
51. Unlocking predictive potential: the frequency-domain approach to equity premium forecasting

**(第 58/65 页)**

---

## 前沿探索：精选之外的研究（续）

52. Improving out-of-sample forecasts of stock price indexes with forecast reconciliation and clustering
53. A Comparative Analysis of Deep Learning and Traditional Statistics for Stock Price and Return Forecasting
54. A Fully Analog Pipeline for Portfolio Optimization

**电子金融市场与LOB**

55. Reinforcement Learning in Non-Markov Market-Making
56. Double Auctions: Formalization and Automated Checkers
57. A Financial Market Simulation Environment for Trading Agents Using Deep Reinforcement Learning
58. Price impact and long-term profitability of energy storage
59. Information Externalities, Free Riding, and Optimal Exploration in the UK Oil Industry

**金融衍生品建模与波动率前沿**

60. Graph-Based Methods for Forecasting Realized Covariances
61. Discrete approximation of risk-based prices under volatility uncertainty
62. A second order finite volume IMEX Runge-Kutta scheme for two dimensional PDEs in finance
63. No arbitrage and the existence of ACLMMs in general diffusion models
64. Numerical analysis of American option pricing in a two-asset jump-diffusion model

**(第 59/65 页)**

---

## 前沿探索：精选之外的研究（续）

65. European Option Pricing in Regime Switching Framework via Physics-Informed Residual Learning
66. Efficient calibration of the shifted square-root diffusion model to credit default swap spreads using asymptotic approximations
67. A Data Driven Study on Fractional Black-Scholes-Merton Equation Using Physics Informed Neural Network
68. Automated Volatility Forecasting
69. Exploiting News Analytics for Volatility Forecasting
70. Multi-model transfer function approach tuned by PSO for predicting stock market implied volatility explained by uncertainty indexes
71. KANOP: A Data-Efficient Option Pricing Model using Kolmogorov-Arnold Networks
72. Forecasting Day-Ahead Eurusd Tail Risk: Leveraging Machine Learning and the Volatility Surface
73. Exact Simulation of Quadratic Intensity Models

**金融市场与宏观经济学新趋势**

74. Mean field equilibrium asset pricing model under partial observation: An exponential quadratic Gaussian approach
75. Responsible Investing under Climate Change Uncertainty
76. Fractional Moments by the Moment-Generating Function
77. Distributionally Robust Instrumental Variables Estimation

**(第 60/65 页)**

---

## 前沿探索：精选之外的研究（续）

78. Macroeconomic Impacts of ETS Revenue Allocation: A Post-Keynesian Analysis of Decarbonization Strategies in the EU
79. Note on Bubbles Attached to Real Assets
80. A Run on Fossil Fuel? Climate Change and Transition Risk
81. Dynamic treatment effect of capital controls on macroeconomic and financial stability in emerging market economies
82. Heterogeneous Economies and Micro Data
83. How Do Electoral Votes, Presidential Approval, and Consumer Sentiment Respond to Economic Indicators?
84. A Hierarchical-Dealer-Centric Model of FX Swap Valuation
85. Is Capital Structure Irrelevant with ESG Investors?
86. Alternative Finance in the International Business Context: A Review and Future Research
87. Dynamic graphical models: Theory, structure and counterfactual forecasting
88. The Hallin-Liška criterion through the lens of the random matrix theory
89. The effects of climate changerelated risks on banks: A literature review
90. Machine Learning Debiasing with Conditional Moment Restrictions: An Application to LATE
91. Reforming the IMF Surcharge Rate Policy to Avoid Procyclical Lending
92. Econometrics of Insurance with Multidimensional Types
93. TimeBridge: Non-Stationarity Matters for Long-term Time Series Forecasting

**(第 61/65 页)**

---

## 前沿探索：精选之外的研究（续）

94. EXPRESS: Addressing Endogeneity Using a Two-stage Copula Generated Regressor Approach
95. Empirical Insights into Financial Development and Climate Policy Uncertainty Paving the Path for Energy Diversification in the US
96. Managerial Overextrapolation: Who and When

**量化风险管理**

97. First order Martingale model risk and semi-static hedging
98. Optimal mutual insurance against systematic longevity risk
99. Corporate Non-Disclosure Disputes: Equilibrium Settlements with a Probabilistic Burden of Proof
100. Risk Aggregation and Allocation in the Presence of Systematic Risk via Stable Laws
101. Applications of the Second-Order Esscher Pricing in Risk Management
102. Worst-case values of target semi-variances with applications to robust portfolio selection
103. Machine learning technique to compute climate risk in finance
104. A dealers funding liquidity risk and its money market trades in the 2007/08 crisis
105. Cryptocurrencies and Systemic Risk. The Spillover Effects Between Cryptocurrency and Financial Markets
106. Skew Index: a machine learning forecasting approach
107. Continuous Risk Factor Models: Analyzing Asset Correlations through Energy Distance

---

## 前沿探索：精选之外的研究（续）

108. Quantum Monte Carlo Integration for Simulation-Based Optimisation
109. Tail risk and uncertainty in financial markets
110. Stochastic Loss Reserving: Dependence and Estimation
111. Examination of Bitcoin Hedging, Diversification and Safe-Haven Ability During Financial Crisis: Evidence from Equity, Bonds, Precious Metals and Exchange Rate
112. Measuring Market Risk in Asset Management
113. Computing Systemic Risk Measures with Graph Neural Networks
114. A Spatio-Temporal Machine Learning Model for Mortgage Credit Risk: Default Probabilities and Loan Portfolios
115. Forecasting VaR and Returns Distribution Using the Real-Time GARCH Models with Standardized Two-Sided Lindley Distribution
116. The Analytics of Robust Satisficing: Predict, Optimize, Satisfice, Then Fortify
117. Risk parity portfolio optimization under heavytailed returns and dynamic correlations
118. Are causal effect estimations enough for optimal recommendations under multi-treatment scenarios?
119. A One-Step Approach for Determining the Optimal Aggregate Capital Reserve and Allocation
120. On the mean-field limit of diffusive games through the master equation: extreme value analysis

---

## 前沿探索：精选之外的研究（续）

**去中心化金融(DeFi)**

121. The Rise of Decentralised Finance (DeFi)
122. Lightning Network Economics: Topology
123. Competitive dynamics between decentralized and centralized finance lending markets
124. Ormer: A Manipulation-resistant and Gas-efficient Blockchain Pricing Oracle for DeFi
125. Improving DeFi Mechanisms with Dynamic Games and Optimal Control: A Case Study in Stablecoins
126. Security Perceptions of Users in Stablecoins: Advantages and Risks within the Cryptocurrency Ecosystem

**时间序列预测**

127. HiMTM: Hierarchical Multi-Scale Masked Time Series Modeling with Self-Distillation for Long-Term Forecasting
128. FlexTSF: A Universal Forecasting Model for Time Series with Variable Regularities
129. Novel Bayesian algorithms for ARFIMA long-memory processes: a comparison between MCMC and ABC approaches
130. Recurrent Neural Goodness-of-Fit Test for Time Series
131. xLSTM-Mixer: Multivariate Time Series Forecasting by Mixing via Scalar Memories
132. Context is Key: A Benchmark for Forecasting with Essential Textual Information

**(第 64/65 页)**

---

## 前沿探索：精选之外的研究（续）

133. Graph Neural Flows for Unveiling Systemic Interactions Among Irregularly Sampled Time Series
134. TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis
135. Timer-XL: Long-Context Transformers for Unified Time Series Forecasting
136. Inferring Latent Graphs from Stationary Signals Using a Graphical Autoregressive Model
137. Metadata Matters for Time Series: Informative Forecasting with Transformers
138. Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift
139. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation
140. Advancing Multivariate Time Series Anomaly Detection: A Comprehensive Benchmark with Real-World Data from Alibaba Cloud
141. Diffusion Auto-regressive Transformer for Effective Self-supervised Time Series Forecasting
142. LLM-Mixer: Multiscale Mixing in LLMs for Time Series Forecasting
143. LLM-TS Integrator: Integrating LLM for Enhanced Time Series Modeling
144. Scalable Signature-Based Distribution Regression via Reference Sets
145. Robustness Auditing for Linear Regression: To Singularity and Beyond
146. On Anticompetitive Third-Degree Price Discrimination

---

*以上为2024年10月量化金融领域的精选论文与额外前沿研究索引，涵盖AI、LLM、投资组合优化、衍生品定价、风险管理、DeFi、宏观经济以及时间序列预测等领域，为研究人员、从业者与政策制定者提供参考与启示。*
