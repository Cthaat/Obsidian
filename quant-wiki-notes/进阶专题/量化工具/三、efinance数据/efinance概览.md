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
