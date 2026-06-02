---
title: AKShare 安装配置
tags: [AKShare, 安装, pip, Docker, Anaconda]
created: 2026-06-02
source: /opt/data/investment/kb/data-tools/akshare-docs/installation.md
parent: "[[AKShare概览]]"
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
