---
title: AKShare 安装配置
tags: [AKShare, 安装, pip, Docker, Anaconda]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/installation.md
parent: "[[AKShare概览]]"
aliases: []
updated: 2026-06-02
---

# AKShare 安装配置

> [!note] 重要前提
> 1. 仅支持 **64 位** 操作系统
> 2. 仅支持 **Python 3.9(64位)** 及以上版本，推荐 **Python 3.11.x(64位)**
> 3. 推荐安装最新版本 [Anaconda (64位)](https://www.anaconda.com/)，可解决大部分环境配置问题
> 4. 程序运行时，文件名、文件夹名**不能**是：`akshare`

## 安装方式

### 通用安装（pip）

```bash
pip install akshare --upgrade
```

### 国内加速安装

```bash
# Python 环境
pip install akshare --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple

# Anaconda 环境
pip install akshare --upgrade --user -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 升级

```bash
pip install akshare --upgrade -i https://pypi.org/simple
```

> **注意**：由于版本更新迭代频繁，请使用前先升级。

## 平台支持

| 平台 | 支持情况 | 说明 |
|------|---------|------|
| Windows 64位 | ✅ 完全支持 | — |
| macOS Intel | ✅ 完全支持 | — |
| macOS M系列 | ✅ 完全支持 | 直接 `pip install` 即可 |
| Linux 64位 | ✅ 完全支持 | — |
| 树莓派 4B | ✅ 支持 | 需 Raspberry Pi OS (64-bit) |

### 树莓派安装步骤

```bash
# 1. 安装 Raspberry Pi OS (64-bit)
# 2. 安装虚拟环境支持
sudo apt-get install python3-venv

# 3. 创建虚拟环境
python3 -m venv myenv

# 4. 激活虚拟环境
source myenv/bin/activate

# 5. 安装 AKShare
pip install akshare --upgrade
```

## Docker 部署

熟悉容器技术的小伙伴可使用 Docker 部署，详见 [AKShare Docker 部署指南](https://akshare.akfamily.xyz/akdocker/akdocker.html)。

## R 语言调用

推荐使用 **AKTools** 项目部署 AKShare 的 HTTP API，运行速度更快，更稳定，兼容各种编程语言。详情参考 [AKTools 文档](https://aktools.readthedocs.io/)。

## 相关笔记
- [[AKShare概览]]
- [[AKShare-股票数据]]

## 实战掌握清单

> [!tip] 交易者视角
> AKShare 安装配置 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

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

围绕 AKShare 安装配置 完成一个可复现任务：获取数据、清洗字段、保存版本、运行简单分析并输出日志。工具页的价值在于让研究链路更稳定。

### 检查点

- 字段含义是否清楚。
- 数据更新时间是否符合策略需求。
- 异常、缺失、限流和失败重试是否被记录。
- 结果是否可以由另一个人复现。

### 边界

工具只是基础设施，不替代策略假设和风险控制。
