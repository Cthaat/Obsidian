---
title: EasyQuant 概览
tags: [EasyQuant, eqlib, 量化框架, 回测, Python]
created: 2026-06-02
source: /opt/data/investment/kb/repos/EasyQuant/
parent: "[[目录|量化工具]]"
aliases: []
updated: 2026-06-02
---

# EasyQuant 概览

> [!note] EasyQuant 简介
> **EasyQuant**（`eqlib`）是一个面向中国 A 股市场的**轻量级量化策略框架**。提供事件驱动的策略 API、免费数据源、完整回测报告生成、Web 策略工作室以及多策略模板。

## 项目信息

| 属性 | 内容 |
|------|------|
| 项目名称 | EasyQuant / eqlib |
| 定位 | A 股量化策略回测框架 |
| 语言 | Python（后端）、TypeScript + React（前端） |
| 开源协议 | MIT |
| 安装方式 | `pip install easyquant-eqlib` |
| Python 要求 | 3.9+（推荐 3.11） |
| 仓库文件 | 100+ 个文件（含前端/后端/教程/测试） |

## 核心定位

EasyQuant 提供：

- **简单直观的策略 API**（事件驱动模式，类似 JoinQuant 风格）
- **免费的 A 股数据源**（通过 akshare 获取）
- **完整的回测 + 报告生成**（HTML 报告，含指标卡片、回撤曲线、交易记录）
- **Web 策略工作室**（浏览器中编写 Python 策略、运行回测、查看报告）
- **可导出到实盘平台**（PTrade/QMT）

## 架构总览

| 组件 | 技术栈 | 说明 |
|------|--------|------|
| **核心库 `eqlib/`** | Python | 策略引擎、回测引擎、数据获取、报告生成 |
| **Web Studio 后端** | FastAPI、SQLAlchemy 2（async）、SQLite | REST API、SSE 流、用户认证、策略 CRUD |
| **Web Studio 前端** | React 18、TypeScript、Vite、Monaco Editor | 70/30 布局、策略编辑、回测运行、报告查看 |
| **教程体系 `tutorials/`** | Markdown（12篇） | 零基础到实盘的完整学习路径 |

## 快速开始

```bash
# 安装
pip install easyquant-eqlib

# 验证
python -c "from eqlib import *; print('eqlib OK')"

# 跑第一份回测（需在仓库目录）
python examples/03_run_backtest.py

# 打开 HTML 报告
# 浏览器中查看 reports/*.html
```

## Web 策略工作室

无需安装 Python 环境，打开浏览器即可编写策略、运行回测：

```bash
cd web_strategy_studio
npm run dev:all    # 同时启动前后端
# 后端: http://127.0.0.1:8080
# 前端: http://localhost:5173
```

## 相关笔记
- [[EasyQuant-教程体系]]
- [[EasyQuant-Web策略工作室]]
- [[EasyQuant-后端架构]]

## 课程化学习补充

> [!important] 学习定位
> 工具服务于研究闭环：获取数据、清洗数据、验证策略、执行交易和复盘监控；选择工具要看稳定性和可维护性。本文仅用于学习、研究与复盘，不构成任何投资建议。

### 必须掌握的问题

- 接口是否稳定
- 数据字段和频率是否满足策略
- 版本是否锁定
- 是否有替代数据源交叉验证

### 实战应用流程

1. 先写清楚你的投资假设：为什么这个信号、资产或方法应该产生收益。
2. 明确数据口径：样本范围、更新时间、复权/分红/停牌处理和交易日历。
3. 做最小可行验证：先用简单规则验证方向，再逐步加入复杂模型。
4. 把成本和约束前置：手续费、滑点、冲击成本、保证金、流动性和容量都要进入测算。
5. 上线后持续复盘：记录信号、下单、成交、持仓、回撤和失效原因。

### 风险与失效条件

- 免费数据缺口
- 网页结构变化导致接口失效
- 版本升级破坏兼容
- 忽视数据授权和合规

### 复盘问题

- 这笔交易或这套模型赚的是什么钱：风险补偿、行为偏差、流动性溢价，还是偶然噪音？
- 如果市场环境反过来，最大亏损和最长恢复期会是多少？
- 当前结论是否依赖某个不可持续假设，例如低利率、低波动、充裕流动性或监管套利？
- 有没有一个更简单的基准策略能取得接近效果？

### 延伸学习

- [[Python量化环境配置]]
- [[AKShare概览]]
- [[VnPy框架详解]]
- [[量化数据源]]
