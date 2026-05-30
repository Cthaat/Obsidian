---
title: "TradeMaster强化学习"
category: "AI+量化"
tags: [AI+量化, 量化, 交易, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

**TradeMaster** 是一款面向量化交易（QT）的开源平台，它将**强化学习（RL）** 技术全面融合到量化交易全流程中。从数据准备、算法实现、评估到部署，TradeMaster为开发者与研究者提供了一套“**一站式**”解决方案。

---

### 一、最新动态

| 更新内容 | 状态 |
| --- | --- |
| 新增 FinAgent 与 EarnMore | 🔨 2024年10月29日更新 |
| 更新 Market Simulator | 🔨 2023年9月21日更新 |
| 更新 Market Dynamics Modeling Tool | 🔧 2023年7月7日更新 |
| 支持自动特征生成与选择 | 🔨 2023年5月11日教程更新 |
| 发布 Python 包 | 🐳 2023年5月11日更新 |
| 搭建 TradeMaster 网站 | 🐳 2023年4月23日 |
| 撰写软件文档 | 💬 2023年4月11日更新 |
| 发布Colab版本 | 💬 2023年3月29日更新 |
| 增加港股与期货数据集 | 🧭 2023年3月27日更新 |
| 支持Alpha158指标 | 🔨 2023年3月20日更新 |
| 正式发布TradeMaster 1.0.0 | 2023年3月5日 |

---

### 二、TradeMaster概览

TradeMaster将量化交易工作流划分为6大模块：

![](https://fastly.jsdelivr.net/gh/bucketio/img12@main/2025/01/29/1738123026827-f604dec0-5a06-4fb4-b186-c296326e624a.png)

1. **多模态市场数据**：涵盖不同金融资产与多种频率；
2. **完整数据预处理流水线**：自动清洗、特征生成等；
3. **高保真市场模拟器**：包含多种主流量化交易场景；
4. **13+ 强化学习算法实现**：大幅提升交易策略效率；
5. **系统化评估工具**：6个维度、17种衡量指标，评估策略表现；
6. **多样化接口**：满足跨学科用户（科研、工程）的需求。

---

### 三、安装与使用

#### 1. 安装方法

- **Linux/Windows/MacOS**
- **Docker**

官方在[[Installation]]里提供了详细的环境配置指南。

#### 2. 核心教程

TradeMaster自带了一系列“样例代码”和**Colab在线教程**，涵盖以下场景：

| 算法 | 数据集 | 市场 | 任务 | 代码 |
| --- | --- | --- | --- | --- |
| EIIE | DJ 30 | 美股 | 投资组合管理 | [[tutorial]] |
| DeepScalper | BTC | 加密货币 | 日内交易 | [[tutorial]] |
| SARL | DJ 30 | 美股 | 投资组合管理 | [[tutorial]] |
| PPO | SSE 50 | A股 | 投资组合管理 | [[tutorial]] |
| ETEO | Bitcoin | 加密货币 | 订单执行 | [[tutorial]] |
| Double DQN | Bitcoin | 加密货币 | 高频交易 | [[tutorial]] |

---

### 四、实用脚本

TradeMaster附带的脚本功能十分丰富：

- **自动超参数调优**
- **自动特征生成**
- **基于扩散模型的数据插值修复**
- **结合Alpha158技术指标进行RL训练**
- **TradeMaster Sandbox 沙盒测试**

此外，还提供Market Dynamics建模工具及相应网站接口。

---

### 五、数据集

平台收录了多种常见的市场数据：

| 数据集  | 来源       | 类型       | 范围与频率           | 数据类型 | 链接 |
| ------- | ---------- | ---------- | -------------------- | -------- | ---- |
| S&P500  | Yahoo      | 美股       | 2000/01/01-2022/01/01, 1day | OHLCV  | [[SP500]] |
| DJ30    | Yahoo      | 美股       | 2012/01/01-2021/12/31, 1day | OHLCV  | [[DJ30]] |
| BTC     | Kaggle     | 外汇       | 2000/01/01-2019/12/31, 1day | OHLCV  | [[FX]]   |
| Crypto  | Kaggle     | 加密货币   | 2013/04/29-2021/07/06, 1day | OHLCV  | [[Crypto]] |
| SSE50   | Yahoo      | A股        | 2009/01/02-2021/01/01, 1day | OHLCV  | [[SSE50]] |
| Bitcoin | Binance    | 加密货币   | 2021/04/07-2021/04/19, 1min | LOB    | [[Binance]] |
| Future  | AKshare    | 期货       | 2023/03/07-2023/03/28, 5min | OHLCV  | [[Future]] |
| HS30    | AKShare    | 港股       | 1988/12/30-2023/03/27, 1day | OHLCV  | [[HS30]] |

可从Google Drive或Baidu Cloud(提取码:x24b)下载。

---

### 六、模型库（Model Zoo）

TradeMaster中包含了多种RL交易算法的高效实现，包括：

- **DeepScalper (CIKM 22)**
- **OPD (AAAI 21)**
- **DeepTrader (AAAI 21)**
- **SARL (AAAI 20)**
- **ETEO (20)**
- **Investor-Imitator (KDD 18)**
- **EIIE (17)**

以及基于Pytorch或Ray的经典强化学习算法，如PPO、A2C、Rainbow、SAC、DDPG、DQN、PG、TD3等。

---

### 七、可视化工具

TradeMaster提供了大量可视化工具，以多维度评估强化学习量化策略。

![](https://fastly.jsdelivr.net/gh/bucketio/img2@main/2025/01/29/1738123100989-f58db4af-6048-40c1-aaf2-1b3adbe6e98c.png)

![](https://fastly.jsdelivr.net/gh/bucketio/img3@main/2025/01/29/1738123086122-b3c91503-802d-4e17-b5c4-fda19faf4838.png)

更多细节可参考相关[[paper]]和[[repo]]。

## 相关论文

- **PRUDEX-Compass**: Systematic Evaluation of RL in Financial Markets (TMLR 2023)
- **Reinforcement Learning for Quantitative Trading (Survey)** (ACM TIST 2023)
- **Deep RL for Quantitative Trading: Challenges & Opportunities** (IEEE Intelligent Systems 2022)
- **DeepScalper** (CIKM 2022)
- **Commission Fee is not Enough** (AAAI 2021)
