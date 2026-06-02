---
title: Fama-French三因子模型
tags:
  - Fama-French
  - 三因子模型
  - 资产定价
  - 学术模型
created: 2026-06-02
type: note
source: fama-french-three-factor-model.md
---

# Fama-French三因子模型

> [!note] Fama-French三因子模型
> Fama-French三因子模型是现代资产定价理论的基石，由Eugene Fama和Kenneth French于1993年提出。它用三个因子来解释股票收益的横截面差异。

## 模型公式

```
R_i - R_f = α_i + β_i^MKT × (R_m - R_f) + β_i^SMB × SMB + β_i^HML × HML + ε_i
```

## 三个因子

### 1. 市场因子（MKT）
- 定义：市场组合收益率减去无风险利率
- 含义：承担系统性市场风险的补偿
- 来源：CAPM的传统因子

### 2. 规模因子（SMB, Small Minus Big）
- 定义：小市值公司收益减去大市值公司收益
- 含义：小公司股票的超额收益
- 历史表现：小盘股长期跑赢大盘股

### 3. 价值因子（HML, High Minus Low）
- 定义：高账面市值比公司收益减去低账面市值比公司收益
- 含义：价值股的超额收益
- 历史表现：价值股长期跑赢成长股

## 因子构建方法

### SMB因子
```
SMB = (小盘股收益均值) - (大盘股收益均值)
```

### HML因子
```
HML = (高B/M股票收益均值) - (低B/M股票收益均值)
```

## 模型意义

- 解释了CAPM无法解释的规模效应和价值效应
- 为多因子投资提供了理论基础
- 因子溢价被视为系统性风险补偿

## 相关链接

- [[Fama-French五因子模型]]
- [[Fama-French实战指南]]
- [[Fama-French数据处理]]
- [[../目录|量化策略总览]]
