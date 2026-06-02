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

## 实战掌握清单

> [!tip] 交易者视角
> EasyQuant 概览 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

### 关键判断

- 确认数据源、字段含义、更新频率、限流和异常值处理。
- 检查工具是否支持复现、日志、版本管理和错误恢复。
- 把接口能力和策略需求对齐，避免为工具而工具。

### 落地动作

1. 建立数据校验、缓存、重试和缺失值报告。
2. 把研究代码、回测代码和实盘代码的差异写清楚。
3. 上线前做小资金、只读或模拟环境验证。

### 失效边界

- 接口字段变更导致结果失真。
- 缺少日志无法追踪错误。
- 把工具稳定性误认为策略有效性。

### 复盘问题

- 这项知识改变了哪一个具体决策：标的、方向、仓位、退出、对冲还是不交易？
- 如果判断相反，最大亏损、最长恢复期和退出触发条件是什么？
- 有没有一个更简单的基准方法可以取得相近结果？

## 深度案例与训练

### 工具小项目

围绕 EasyQuant 概览 完成一个可复现任务：获取数据、清洗字段、保存版本、运行简单分析并输出日志。工具页的价值在于让研究链路更稳定。

### 检查点

- 字段含义是否清楚。
- 数据更新时间是否符合策略需求。
- 异常、缺失、限流和失败重试是否被记录。
- 结果是否可以由另一个人复现。

### 边界

工具只是基础设施，不替代策略假设和风险控制。
