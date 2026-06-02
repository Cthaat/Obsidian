---
title: efinance 概览
tags: [efinance, 财经数据, Python, 开源]
created: 2026-06-02
source: /opt/data/investment/kb/doc-sites/efinance-数据/
parent: "[[目录|量化工具]]"
aliases: []
updated: 2026-06-02
---

# efinance 概览

> [!note] efinance 简介
> **efinance** 是由个人打造的用于获取股票、基金、期货数据的免费开源 Python 库，使用它可以很方便地获取数据以服务于个人的交易系统需求。

## 项目信息

| 属性 | 内容 |
|------|------|
| 项目名称 | efinance |
| 当前版本 | **0.5.8**（latest） |
| Python 要求 | 3.6+ |
| 开源协议 | 开源免费 |
| 作者 | Micro-sheep |
| 仓库地址 | [github.com/Micro-sheep/efinance](https://github.com/Micro-sheep/efinance) |
| 文档地址 | [efinance.readthedocs.io](https://efinance.readthedocs.io) |
| 文档来源 | 24 个版本文件（v0.3.3 ~ v0.5.8） |

> **郑重声明**：本项目仅供学习交流使用，不得用于商业用途。

## 安装方式

### pip 安装

```bash
pip install efinance
pip install efinance --upgrade   # 更新
```

### Docker 安装

```bash
git clone https://github.com/Micro-sheep/efinance
cd efinance
docker build -t efinance . --no-cache
docker run --rm -it efinance
```

### 源码安装（开发用）

```bash
git clone https://github.com/Micro-sheep/efinance
cd efinance
pip install -e .
```

## 核心模块

`efinance` 采用简洁的模块化设计：

```
ef
├── stock    — 股票数据
├── fund     — 基金数据
├── futures  — 期货数据
└── bond     — 债券数据（后续版本）
```

## 快速示例

### 获取股票历史日K线

```python
import efinance as ef

# A股
ef.stock.get_quote_history('600519')  # 贵州茅台，从 2001年至今

# 非A股（支持代码和名称）
ef.stock.get_quote_history('AAPL')    # 苹果，从 1984年至今
```

### 获取基金数据

```python
import efinance as ef

ef.fund.get_quote_history('161725')  # 招商中证白酒
```

### 获取期货数据

```python
import efinance as ef

ef.futures.get_quote_history('RB888')
```

## 与 AKShare 的定位差异

| 对比维度 | efinance | AKShare |
|---------|----------|---------|
| 数据覆盖 | 股票、基金、期货（核心品类） | 全品类：股票/期货/期权/债券/外汇/宏观/加密等 |
| API 风格 | 极简，模块化（`ef.stock.*`） | 函数式，大量以数据源命名的接口 |
| 文档规模 | 简洁 | 完备（每个接口都有参数表+示例） |
| 社区规模 | 较小 | 大型社区（10k+ GitHub Stars） |
| 适合场景 | 快速获取常见行情数据 | 深度研究、学术分析、全品类数据 |

## 版本跨度

efinance 文档覆盖 24 个版本（v0.3.3 ~ v0.5.8），每版包含更新日志和 API 变化。详见 [[efinance-版本演进]]。

## 相关笔记
- [[efinance-常用接口]]
- [[efinance-版本演进]]
- [[AKShare概览]]

## 实战掌握清单

> [!tip] 交易者视角
> efinance 概览 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

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
