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

## 跨领域进阶扩展

> [!tip] 交易者视角
> 学到 `AKShare 安装配置` 时，不要只把它当成孤立知识点。把工具纳入研究闭环，选择标准是可靠、可复现、可替代。优秀投资交易者会把它放入“宏观背景 - 资产选择 - 估值/信号 - 组合风险 - 交易执行 - 复盘反馈”的闭环。

### 与其他知识的连接

- 数据字段、频率和授权
- 版本锁定和环境隔离
- 接口限频和异常处理
- 替代数据源交叉验证

### 进阶训练

1. 用两个数据源抽样核对同一字段
2. 记录依赖版本和数据下载时间
3. 给接口失败写降级方案

### 能力验收

- 能否说清楚这个主题影响的是收益来源、风险来源、交易成本、流动性还是心理纪律？
- 能否指出它在什么市场环境、资产类别或交易周期中更有效？
- 能否把它写成一条可复盘的研究或交易规则？
- 能否说明如果判断错误，组合最大损失和退出机制是什么？

### 全局关联

- [[综合金融知识体系/金融投资全知识地图|金融投资全知识地图]]
- [[综合金融知识体系/优秀投资交易者能力地图|优秀投资交易者能力地图]]
- [[综合金融知识体系/一次性学习路线与复盘模板|一次性学习路线与复盘模板]]
