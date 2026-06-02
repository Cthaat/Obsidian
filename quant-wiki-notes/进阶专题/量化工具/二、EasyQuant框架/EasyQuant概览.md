---
title: EasyQuant 概览
tags: [EasyQuant, eqlib, 量化框架, 回测, Python]
created: 2026-06-02
source: /opt/data/investment/kb/repos/EasyQuant/
parent: "[[目录|量化工具]]"
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
