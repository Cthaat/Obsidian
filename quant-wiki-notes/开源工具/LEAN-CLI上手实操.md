---
title: LEAN-CLI上手实操
date: 2026-07-13
tags:
  - 开源工具
  - LEAN
  - QuantConnect
  - 实操
---

# LEAN-CLI上手实操

> [!note] 核心问题
> [LEAN CLI](https://www.quantconnect.com/docs/v2/lean-cli/key-concepts/getting-started) 把开源 [LEAN](https://github.com/QuantConnect/Lean) 引擎包成命令行，可本地/云端回测。适合已会 QC 云端算法、要工程化的人。**以官网文档当前要求为准**（会员层级、Docker 等可能变化）。

## 学习目标

1. 知道 CLI 与网页 Algorithm Lab 的分工。  
2. 列出安装前置：Python/pip、Docker、账号登录。  
3. 走通 `lean login` → `lean init` → `lean backtest` 心智路径。  
4. 理解数据需单独准备/下载。  
5. 不把本地回测默认当零成本实盘。  

## 前置（文档要点）

官方 Getting Started 常见要求包括：

| 项 | 说明 |
|---|---|
| 组织/会员 | 部分本地引擎能力与 QC 组织层级相关（**以账号页与文档为准**） |
| pip | 推荐正规 Python/Anaconda；避免不当来源解释器 |
| Docker | 本地 engine 命令通常需要 Docker 在运行 |
| 登录 | `lean login` 使用 User Id 与 API Token |

安装：

```text
pip install lean
```

## 工作区初始化

在空目录：

```text
lean login
lean init
```

会生成工作区配置（如 `lean.json`）与示例数据结构（以实际输出为准）。**之后命令都在该工作区执行。**

## 第一回测路径

| 步骤 | 命令思想 |
|---|---|
| 拉云项目（可选） | `lean cloud pull` |
| 准备数据 | 文档中的 data generate / 下载 / 自有数据转换 |
| 本地回测 | `lean backtest "<projectName>"`（Docker 跑引擎） |
| 云回测 | `lean cloud backtest "<projectName>"`（可先 push） |

细节与参数以 [LEAN CLI 文档](https://www.quantconnect.com/docs/v2/lean-cli/key-concepts/getting-started) 为准。

## 与 QuantConnect 上手文关系

| 文 | 重点 |
|---|---|
| [[QuantConnect上手实操]] | 网页项目、Initialize 结构 |
| 本文 | 本地 CLI、Docker、工作区 |

建议顺序：先云端跑通官方示例 → 再 CLI。

## 常见坑

| 坑 | 处理 |
|---|---|
| Docker 未开 | 先启动 Docker |
| Windows 文件共享 | 按文档给工作区授权 |
| 无数据 | 不要空跑；按文档生成/下载 |
| 权限/会员不足 | 读账号与文档，不猜 |

更多：[[开源工具常见坑]]。

## 练习

| 项 | 完成 |
|---|---|
| lean 版本 |  |
| 工作区路径 |  |
| 是否完成一次 backtest |  |
| 卡点记录 |  |

## 相关概念

[[QuantConnect上手实操]] [[工具实操总导航]] [[开源工具常见坑]] [[回测方法论]]
