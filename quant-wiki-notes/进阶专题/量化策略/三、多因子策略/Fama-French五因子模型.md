---
title: Fama-French五因子模型
tags:
  - Fama-French
  - 五因子模型
  - 盈利因子
  - 投资因子
created: 2026-06-02
type: note
source: fama-french-five-factor-model.md, bigquant-five-factor-explained.md, bigquant-fama-french-5factor.md
---

# Fama-French五因子模型

> [!note] 五因子模型
> Fama-French五因子模型在三因子基础上增加了盈利因子（RMW）和投资因子（CMA），于2015年提出，是目前学术界和业界最广泛使用的资产定价模型之一。

## 模型公式

```
R_i - R_f = α_i + β₁×MKT + β₂×SMB + β₃×HML + β₄×RMW + β₅×CMA + ε_i
```

## 五个因子详解

| 因子 | 全称 | 含义 | 构建方法 |
|-----|------|------|---------|
| MKT | Market | 市场超额收益 | 市场组合收益 - 无风险利率 |
| SMB | Small Minus Big | 小盘溢价 | 小市值组合 - 大市值组合 |
| HML | High Minus Low | 价值溢价 | 高B/M组合 - 低B/M组合 |
| RMW | Robust Minus Weak | 盈利溢价 | 高盈利组合 - 低盈利组合 |
| CMA | Conservative Minus Aggressive | 投资溢价 | 保守投资组合 - 激进投资组合 |

## 盈利因子（RMW）

- **定义**：高营业利润率公司收益减去低营业利润率公司收益
- **逻辑**：盈利能力强的公司持续表现更好
- **指标**：营业利润率（Operating Profitability）

## 投资因子（CMA）

- **定义**：保守投资公司收益减去激进投资公司收益
- **逻辑**：过度投资的公司往往回报较低
- **指标**：总资产增长率（Asset Growth）

## 与三因子模型的比较

| 方面 | 三因子模型 | 五因子模型 |
|-----|----------|----------|
| 因子数 | 3 | 5 |
| 解释力 | 较强 | 更强 |
| 价值因子 | 显著 | 被盈利和投资因子部分替代 |
| 提出时间 | 1993 | 2015 |

## 相关链接

- [[Fama-French三因子模型]]
- [[Fama-French实战指南]]
- [[多因子策略核心原理]]
- [[../目录|量化策略总览]]
