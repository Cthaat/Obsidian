---
topic: 量化部署
parent: 交易平台
tags: [resources, learning, quant-dev]
created: 2026-06-02
---

# Awesome-QuantDev-Learn

> [!note] 概述
> [Awesome-QuantDev-Learn](https://github.com/0voice/Awesome-QuantDev-Learn) 是量化开发领域的系统化学习资源集合，覆盖从基础到进阶的完整知识体系。

## 知识体系

### 金融基础

- 金融市场与交易机制
- 衍生品定价基础
- 资产定价理论（CAPM、APT、Fama-French）
- 固定收益基础

### 数学与统计

- 概率论与数理统计
- 时间序列分析（ARIMA、GARCH）
- 随机过程
- 最优化方法
- 贝叶斯统计

### 编程与工具

| 语言 | 量化用途 |
|------|---------|
| Python | 策略研究、回测、数据分析（主力） |
| C++ | 高频交易、底层执行引擎 |
| SQL | 数据查询、分析报表 |
| R | 统计建模（部分场景） |

### 量化框架

- **vnpy**：国内最完整的量化交易框架
- **Backtrader**：通用回测框架
- **qlib**（微软）：AI量化平台
- **WonderTrader**：C++高性能框架
- **Hikyuu**：系统化交易框架

### 数据源

- 国内：akshare、Tushare、JQData、Wind
- 国外：yfinance、Alpha Vantage、Polygon.io
- 另类数据：卫星图像、社交媒体、供应链

## 学习路径

```
阶段1: 基础入门（1-2个月）
├── Python基础
├── 金融市场基础
└── 第一个回测策略

阶段2: 工具掌握（2-4个月）
├── Backtrader/vnpy实战
├── 数据获取与清洗
└── 策略开发与评估

阶段3: 进阶研究（4-8个月）
├── 因子挖掘与组合
├── ML/DL模型应用
└── 风控与组合优化

阶段4: 生产实战（8-12个月）
├── 系统架构设计
├── 实盘部署与运维
└── 持续优化迭代
```

## 推荐书籍

| 阶段 | 书籍 |
|------|------|
| 入门 | 《打开量化投资的黑箱》 |
| 策略 | 《151 Trading Strategies》 |
| ML | 《Machine Learning for Trading》（Stefan Jansen） |
| 系统 | 《C++ High Performance Trading》 |
| 风控 | 《Risk Management and Financial Institutions》 |
