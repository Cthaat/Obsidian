---
title: "2024金融领域人工智能**精华文献**回顾"
category: "AI+量化"
tags: [AI+量化, 量化, 交易, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# 2024金融领域人工智能**精华文献**回顾

![](https://fastly.jsdelivr.net/gh/bucketio/img9@main/2024/10/20/1729465031968-b3c8959e-1d37-4b8a-91b1-b0b0dfe25143.png)

在过去的两年中，随着生成式人工智能（Generative AI）与大型语言模型（LLMs）技术的飞速发展，金融领域的前沿研究和应用也迎来新一轮的革新。本文旨在汇总、梳理与展示 过去两年在定量金融与 LLM 交叉领域具有代表性的**关键学术论文**及**实践案例**。通过对历史演进、方法论挑战、应用场景与评估基准的系统性介绍，本综述为读者提供一个清晰的导览图，帮助从业者与研究者更好地理解并利用 LLM 技术推动金融领域的创新与变革。

## 内容目录
  
1. LLM 的发展简史  
2. LLM 的一般应用场景  
3. FinLLMs 的方法论、应用及挑战  
4. 金融 LLM 的全景图  
5. 48 篇金融领域 Generative AI 关键论文目录  
   - 金融预测、投资策略与风险管理  
   - 情感分析与文本挖掘  
   - 时间序列分析与预测  
   - LLM 开发（微调）与金融数据整合  
   - 金融 LLM 的评估与基准测试  

---

### LLM 的发展简史  

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/12/14/1734186113125-da5c35e4-7718-45c6-9e72-e60a09c42d87.png)

---

### LLM 的一般应用场景

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2024/12/14/1734186140553-0f9c1d40-6c10-4dd6-857e-5edd165fb9e3.png)

- **Fine Tuning（微调）**：  
  将通用 LLM 调整为特定领域的专家。先从具备广泛知识的 LLM 出发，然后用特定领域的数据对其进行定向训练，使其理解专业文件（如医疗记录、法律文件），并胜任相关任务。

- **Prompt Engineering（提示工程）**：  
  若无法为 LLM 提供足够的微调数据，可通过为模型设计巧妙指令和提示，引导其在数据不足的情况下仍能高效执行特定任务。

- **RAG（Retrieval-Augmented Generation）**：  
  当缺乏合适的微调数据或提示数据时，为 LLM 提供可检索的大型数据仓库。LLM 通过搜索与查询内容相似的文本，利用文本嵌入与编码技术，找到相关信息，以弥补知识盲区，增强回答的参考性。

- **COT（Chain of Thoughts）链式思考**：  
  帮助 LLM 将复杂问题分解为若干小步骤，更深入地进行逻辑推理。

- **Agent CodeLLM（带求解器的 LLM）**：  
  如 Code Interpreter，可直接对代码和数据进行处理。

- **Agent LLM 与搜索引擎集成**：  
  如 “perplexity”，使 LLM 能利用搜索引擎获取实时信息回答复杂查询。

- **Self-Reflection（自我反思）**：  
  LLM 对自身输出进行评估，从不同回答中选择最合适的结果，以提高准确度和相关性。

- **Multishot Prompting（多示例提示）**：  
  在同一提示中提供多个示例，使 LLM 更好地理解任务，从而输出更高质量、更精确的回答。

- **Hallucinations/Machine Unlearning/Safety（幻觉/机器遗忘/安全）**：  
  由于数据质量、生成方法偏差、概率特性、高温度设置或误导性提示等因素，LLM可能产生不符合事实的回答，需要安全策略与模型改进来降低此类风险。

### FinLLMs 的方法论、应用与挑战

- **应用场景**：  
  - 市场新闻情感分析  
  - 财务报告风险评估  
  - 自动化金融建议  
  - 自动交易策略  
  - 欺诈检测  
  - 客户服务机器人  
  - 市场趋势分析

- **挑战**：  
  - 数据隐私与安全  
  - 模型可解释性  
  - 偏差消减  
  - 与现有系统的无缝集成  
  - 准确回测（避免 GPT 模型时序信息泄漏）

- **未来方向**：  
  - 增强模型透明度  
  - 探索无监督学习机会  
  - 制定金融领域 AI 的伦理规范

选择合适的方法将显著影响模型在特定金融任务中的有效性。

### 金融 LLM 的全景图

![](https://fastly.jsdelivr.net/gh/bucketio/img18@main/2024/12/14/1734187108044-881dd1ac-af20-447a-bc58-511eb0d6941c.png)

### 金融预测、投资策略与风险管理

- [ChatGPT Stock Forecasting](): 利用 ChatGPT 分析新闻情感预测股票

> [!note] 股票
> 公司所有权的凭证，代表股东对公司资产和收益的权益
收益，显著优于传统方法。

- [FinancialStatementAnalysis](): LLM 使用财报文本预测企业盈余变动，表现优于人类分析师。

- [Ploutos](): 引入可集成文本与数值数据的金融 LLM 框架，提升股票预测准确度与可解释性。

- [QuantAgent](): 自我提升的量化投资 LLM Agent，通过双层学习流程增强金融预测与信号挖掘。

- [MarketSenseAI](): 利用 GPT-4 分析多元数据，为股票选择提供卓越绩效。

- [RiskLabs](): 基于 LLM 的风险模型在预测市场波动和 VaR 上领先于传统及 AI 模型。

- [LOB-LLM](): 通过端到端自回归模型对订单簿信息进行预测，相关性表现优异。

- [Alpha-GPT](): 将人类纳入决策循环，实现高效、精准的量化投资。

- [LLMFinAdvice](): LLM 在提供可执行的投资建议中，基础与大型模型优于小型微调模型。

- [LLMsCostROI](): 利用决策理论评估 LLM 成本与收益，分析投资回报率与盈利潜力。

- [SystemicRisk](): 利用 LLM 嵌入与知识图谱评估金融新闻中的系统性风险，发现美国金融机构间互联性较低。

### 情感分析与文本挖掘

- [FinLlama](): 基于 Llama 2 7B 微调的金融情感分析模型，更好地理解上下文并在波动市场中具有稳健性。

- [BioFinBERT](): 专注生物科技领域新闻稿对股价影响的金融情感分析。

- [SALLMRef](): 评估 ChatGPT 等 LLM 在情感分析中的表现，LLM 在少样本学习上有优势但在复杂任务上仍受限。

- [SentiEval](): 提出 SENTIEVAL 基准，用于全面评估 LLM 在情感分析任务中的表现。

- [FinSentGPT](): 基于 ChatGPT 微调的金融情感模型，支持多语言并优于现有模型。

- [CryptoSentiment](): 微调 GPT-4 在加密货币情感分析中优于 BERT 和 FinBERT。

- [FinancialTextAnalytics](): JPMorgan 研究评估 ChatGPT 和 GPT-4 在金融文本分析中的优劣。

- [NumLLM](): 利用中文金融教材训练的模型，在数值类金融问题理解上显著优于现有模型。

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2024/12/14/1734186490555-6ddcb578-42e2-4925-a748-e5df8030cc69.png)

### 时间序列分析与预测

- [LLM-TimeSeries](): JPMorgan 对 LLM 在时间序列理解能力的系统评估及分类法研究。

- [TimeGPT-1](): 预训练的时间序列预测基础模型，在零样本下超越传统统计、机器学习和深度学习方法。

- [TiMaGPT](): Time Machine GPT，对历史数据进行时间自适应训练，避免未来数据泄露。

- [SEEDS-GEE-WeatherForecast](): 利用扩散模型的天气预测仿真，为大宗商品交易提供新思路。

- [LLMsStochasticFiltering](): MoE-F 算法动态融合多预训练 LLM 的预测，F1 指标有大幅提升。

- [LLMsDistributionalShifts](): JPMorgan 提出框架利用 LLM 和 API 收集多元时间序列数据，应对分布偏移。

- [AnomalyDetection](): 利用 LLM 嵌入提高金融异常检测的准确率。

### LLM 开发（微调）与金融数据整合

- [BloombergGPT](): 首个将金融数据与文本数据相结合的专用金融 LLM。

- [FinGPT](): 开源金融 LLM，利用 RLHF 技术进行微调。

- [FinMEM](): 具有人类对齐记忆机制的 LLM Agent，用于自动交易。

- [FinAgent](): 多模态金融交易基础 Agent，融合多源数据、工具扩展和高级推理。

- [FinTextQA](): 金融问答数据集，Baichuan2-7B 表现接近 GPT-3.5-turbo。

- [FinGPT-RLSP](): FinGPT 利用 RLSP 从多元实时数据中自动采集并微调，提高实时处理能力。

- [FinTral](): 基于 Mistral-7b 的多模态金融 LLM 套件，适应多样数据类型与领域训练。

- [Shai](): 面向资产管理领域的 10B 参数级别 LLM。

- [FinVerse](): 具备 600+ API 的金融 Agent 系统，利用 LLM 驱动的 SFT 增强数据分析。

- [FinRobot](): 开源平台，将专用 AI Agent 与金融分析相融合，提升分析与决策效率。

- [BlackScholesInDiffusionModels](): 将 Black-Scholes 算法引入扩散模型提示混合中，生成更逼真的图像。

- [FLAN-FinXC](): 基于 FLAN-T5 与 LoRA 微调，在金融数值标注任务中表现出色。

### 金融 LLM 的评估与基准测试

- [LLM-InvestingRationality](): 提出经济理性评估方法，GPT-4 Turbo 在 14 个 LLM 中表现最佳。参见 [Are Large Language Models Rational Investors?]()。

- [FinBen](): 面向金融领域的开源 LLM 评估基准，包括 35 个数据集和 23 个任务。

- [FinLLMs](): 金融领域 LLM 调查研究。

- [LLMsRiskProfile](): 当 LLM 对齐人类伦理后表现更风险厌恶，影响经济决策与投资行为。

- [LLMsEffectOnCryptoLiquidity](): AI 革命提升加密货币市场效率与流动性，特别在 ChatGPT-3 发布后。

- [AutoGPT](): 将 LLM 能力扩展至复杂推理与协作任务。

- [FinGPT-Benchmark](): 通过指令微调评估开源金融 LLM 整合与基准测试的多样性和性能。

- [Portfolio with GenAI](): 利用图模型实现成本高效的投资组合复制，满足投资者偏好并保持高相关性与稳定性。

- [FinGen](): 提出三项前瞻性金融论点生成任务，利用证据、图表和新闻，彰显当前难点。

- [AIinFinance](): 国际清算银行（BIS）研究生成式 AI 对金融中介、保险、资管和支付领域的影响，同时提出对金融稳定与监管的新挑战。

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募

> [!note] 私募
> 向特定投资者（如对冲基金

> [!note] 对冲基金
> 采用多种策略（包括杠杆、卖空等）的投资基金
、银行）非公开发行证券
等一流企业。
