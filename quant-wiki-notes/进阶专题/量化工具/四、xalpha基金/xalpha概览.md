---
title: xalpha 概览
tags: [xalpha, 基金分析, Python, 开源]
created: 2026-06-02
source: /opt/data/investment/kb/doc-sites/xalpha-基金/
parent: "[[目录|量化工具]]"
---

# xalpha 概览

> [!note] xalpha 简介
> **xalpha** 是一个专注于**基金分析与管理**的 Python 库，提供基金信息查询、净值跟踪、交易处理、组合管理、策略回测和定时提醒等一系列功能。

## 项目信息

| 属性 | 内容 |
|------|------|
| 项目名称 | xalpha |
| 当前版本 | **v0.12.4**（latest） |
| 作者 | refraction-ray |
| 仓库地址 | [github.com/refraction-ray/xalpha](https://github.com/refraction-ray/xalpha) |
| 文档地址 | [xalpha.readthedocs.io](https://xalpha.readthedocs.io) |
| 文档来源 | 35 个版本文件（v0.0.6 ~ v0.12.3） |
| 版权 | ©2018, refraction-ray |

> 🚀 **新功能**：xalpha 推出了 **xalpha Agent Native**，支持自然语言驱动的量化分析。

## 核心功能一览

| 功能模块 | 说明 |
|---------|------|
| **基金和指数信息** | 获取基金/指数的基本信息、净值、持仓等 |
| **单一标的交易处理** | 记录和管理单一基金的买卖交易 |
| **基金组合管理分析** | 管理多只基金组成的投资组合 |
| **基金交易策略与回测** | 定义交易规则并进行历史回测 |
| **监视和定时提醒** | 对策略信号进行监控并发送提醒 |
| **通用数据获取器** | 日线和实时数据的统一获取接口 |

## 快速开始

```bash
pip install xalpha
```

### 获取基金信息

```python
import xalpha as xa

# 获取基金基本信息
fund = xa.fundinfo("000001")
print(fund)

# 获取基金净值
fund = xa.fundinfo("161725")
print(fund.price())
```

### 基金组合管理

```python
# 创建多基金组合
portfolio = xa.portfolio(
    ["000001", "161725", "513100"],
    weights=[0.3, 0.4, 0.3]
)
```

## 文档体系

| 文档 | 内容 |
|------|------|
| 快速开始 | 基金信息、交易处理、组合管理、回测、监控 |
| 具体示例 | 基本用法 + 研究案例 |
| 高级用法 | 缓存、可视化、数据本地化、QDII预测、动态回测 |
| 开发者文档 | 工作流、贡献方向、FAQ |
| xalpha API | 完整的 API 参考文档 |

## 版本跨度

xalpha 文档覆盖 33 个版本（v0.0.6 ~ v0.12.3），从 2020 年持续维护至今。详见 [[xalpha-版本演进]]。

## 与其他量化工具的关系

| 工具 | xalpha 的定位 |
|------|-------------|
| [[AKShare概览\|AKShare]] | 数据互补：AKShare 提供全品类原始数据，xalpha 专注基金分析和策略 |
| [[efinance概览\|efinance]] | 品类不同：efinance 提供股票/基金/期货行情，xalpha 提供基金深度分析 |
| [[EasyQuant概览\|EasyQuant]] | 定位互补：EasyQuant 做 A 股策略回测，xalpha 做基金组合管理 |

## 相关笔记
- [[xalpha-核心功能]]
- [[xalpha-高级用法]]
- [[xalpha-版本演进]]
