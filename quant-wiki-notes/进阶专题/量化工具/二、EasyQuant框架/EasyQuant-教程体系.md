---
title: EasyQuant 教程体系
tags: [EasyQuant, 教程, 量化学习, 策略开发]
created: 2026-06-02
source: /opt/data/investment/kb/repos/EasyQuant/tutorials/
parent: "[[EasyQuant概览]]"
---

# EasyQuant 教程体系

> [!note] 教程概述
> EasyQuant 提供**12 篇结构化教程**，从零基础到实盘部署，涵盖趋势跟踪、均值回归、行业轮动和多因子选股等方向。

## 教程目录

### 前置知识（按需阅读）

| 序号 | 文件 | 内容摘要 | 预计用时 |
|------|------|---------|---------|
| 前置 | Python 基础与环境配置 | 语法速查、pandas/numpy 核心用法、虚拟环境 | 20 min |
| 前置 | 技术分析基础概念 | OHLCV、MA/RSI/MACD/布林带/ATR/KDJ/ADX | 25 min |
| 前置 | A 股市场基础知识 | 代码格式、T+1、涨跌停、指数、ST股、手续费 | 20 min |

### 核心教程

| 序号 | 标题 | 内容 | 预计用时 |
|------|------|------|---------|
| 00 | **环境与第一次运行** | 安装、首跑回测、打开 HTML 报告（必读） | 30 min |
| 01 | **量化基础概念** | 策略要素、完整流程、新手10个常见错误 | 45～60 min |
| 02 | **编写双均线策略** | `initialize()`、`market_open()`、order API | 60 min |
| 03 | **回测报告解读** | 收益曲线、回撤、夏普比率、最大回撤等指标 | 45 min |
| 04 | **策略参数优化** | 网格搜索、遗传算法调参、归因分析 | 60 min |
| 05 | **模拟盘到实盘** | PTrade/QMT 平台导出、实盘部署流程 | 45 min |
| 06 | **RSI 均值回归策略** | RSI 指标原理、超买超卖信号、止盈止损 | 45 min |
| 07 | **行业轮动策略** | 行业动量/反转、申万行业分类、板块轮动 | 60 min |
| 08 | **多因子选股** | 因子构建、IC/IR检验、分层回测 | 75 min |
| 09 | **综合策略** | 全天候 Alpha 多策略组合 | 60 min |
| 10 | **AI 策略优化** | LLM Agent 自动参数优化与审计 | 45 min |

## 新手首日打卡流程

```bash
# 1. 安装
pip install easyquant-eqlib
python -c "from eqlib import *; print('eqlib OK')"

# 2. 跑第一份完整报告
python examples/03_run_backtest.py

# 3. 打开 reports/*.html 查看指标卡片、回撤曲线、交易记录

# 4. 本地数据快速验证（可选）
python examples/19_local_data_backtest.py --download-all
python examples/19_local_data_backtest.py

# 5. 最小功能验证（可选）
python examples/01_fetch_data.py
pip install -e ".[dev]"
python -m pytest tests/
```

## 量化策略核心要素（来自 Tutorial 01）

任何一个可运行的量化策略包含 5 个要素：

| 要素 | 说明 | 示例 |
|------|------|------|
| **股票池**（Universe） | 操作哪些股票 | 沪深300成分股、白酒板块、固定列表 |
| **入场条件**（Entry） | 何时买入 | 金叉、RSI超卖、动量排名、事件驱动 |
| **出场条件**（Exit） | 何时卖出 | 死叉、止损(-5%)、止盈(+20%回落5%) |
| **仓位管理**（Sizing） | 买多少 | 全仓、等权、凯利公式、风险平价 |
| **风控规则**（Risk） | 如何控制风险 | 最大回撤阈值、持仓上限、分散化 |

## 常见量化策略类型

| 类型 | 原理 | 对应教程 |
|------|------|---------|
| 趋势跟踪 | 顺势而为，追踪已经形成的趋势 | Tutorial 02 |
| 均值回归 | 价格会回归均值，赌反转 | Tutorial 06 |
| 行业轮动 | 不同行业在不同周期有超额收益 | Tutorial 07 |
| 多因子选股 | 用多个因子（PE/PB/动量等）打分选股 | Tutorial 08 |
| 组合策略 | 多策略叠加增强稳健性 | Tutorial 09 |

## 相关笔记
- [[EasyQuant概览]]
- [[EasyQuant-Web策略工作室]]
