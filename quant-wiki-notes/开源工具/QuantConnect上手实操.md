---
title: QuantConnect上手实操
date: 2026-07-13
tags:
  - 开源工具
  - QuantConnect
  - 回测
  - 实操
---

# QuantConnect上手实操

> [!note] 核心问题
> [QuantConnect](https://www.quantconnect.com/) 提供云端研究/回测与开源引擎 **LEAN**，覆盖多资产与较长历史数据，适合英语文档友好的学习者做**全球市场与工程化算法**练习。本篇给「从注册到第一个算法结构」的地图。

## 学习目标

1. 知道 QC 解决云端多资产研究与 LEAN 引擎问题。  
2. 完成注册并找到 Algorithm Lab / 文档。  
3. 理解 `Initialize`、数据订阅、调度与再平衡的基本结构。  
4. 会用文档示例改一个最小逻辑。  
5. 清楚免费额度与数据条款以官网为准。  

## 它是什么

| 维度 | 说明 |
|---|---|
| 平台 | 研究、回测、优化、实盘对接（产品线以官网为准） |
| 引擎 | LEAN（可云端或本地 CLI） |
| 语言 | 主推 **Python** 与 **C#** |
| 数据 | 多资产；点-in-time 等设计是其卖点之一（细节见文档） |

入口：  

- 平台：[https://www.quantconnect.com/](https://www.quantconnect.com/)  
- 文档：[https://www.quantconnect.com/docs/v2](https://www.quantconnect.com/docs/v2)  
- LEAN：[https://github.com/QuantConnect/Lean](https://github.com/QuantConnect/Lean)  

## 谁适合

| 适合 | 不太适合当唯一工具 |
|---|---|
| 练美股/多资产/期权等 | 只做 A 股且需要中文社区答疑 |
| 想要机构向数据与算法结构 | 完全不想读英文文档 |
| 云端少运维 | 必须本地隐私全离线 |

A 股主线仍建议：阶段零 + 聚宽/本地 AKShare。QC 作**第二条市场线**。

## 算法骨架（思想）

文档中的入门模式通常是：

```text
class MyAlgorithm(QCAlgorithm):
    def Initialize(self):
        # 设置起止日期、资金、基准
        # AddEquity / AddUniverse ...
        # 指标预热、Schedule 再平衡

    def OnData(self, data):
        # 或主要用 Schedule 回调，而不堆在 OnData

    # OnSecuritiesChanged ... 宇宙变化时挂指标
```

新手按官方 *Writing Algorithms → Getting Started* 做，比抄随机论坛策略安全。

## 第一小时清单

| 分钟 | 动作 |
|---:|---|
| 0–10 | 注册，进入文档 Getting Started |
| 10–20 | 新建项目（Cloud） |
| 20–45 | 打开官方示例，跑一次回测 |
| 45–55 | 只改一处：标的或再平衡频率 |
| 55–60 | 记录：项目名、参数、结果截图位置 |

本地 CLI（可选进阶）：文档中的 `lean` CLI / `pip install lean` 流程（以当前文档为准）。

## 与聚宽 / quant-lab 对照

| 点 | QuantConnect | 聚宽 | quant-lab |
|---|---|---|---|
| 语言环境 | 云 + LEAN | 云研究 | 本地脚本 |
| 数据 | 多资产强 | A 股生态强 | 自备 |
| 作业成本 | 英文 | 中文 | 工程规范 |
| 迁移 | LEAN 本地 | 出平台难 | 天然本地 |

## 学习纪律

| 做 | 不做 |
|---|---|
| 先跑官方示例 | 一上来实盘经纪账户 |
| 读费用与成交模型设置 | 默认零成本 |
| 样本外思考 | 参数刷到完美曲线 |

## 常见误区

| 误区 | 更好的理解 |
|---|---|
| 云回测=实盘可迁移 | 仍有延迟、权限、心理 |
| 宇宙选股很强就复杂化 | 先等权再平衡示例 |
| 只用 QC 丢弃 A 股主线 | 可双轨，主市场保持一个 |

## 练习

| 项 | 完成 |
|---|---|
| 账号与项目名 |  |
| 官方示例回测成功 |  |
| 你改动的唯一变量 |  |
| 是否作为主市场工具 | 是/否 |

## 相关概念

[[工具实操总导航]] [[国内量化平台对比与上手]] [[回测框架选型与最小示例]] [[网站工具与资源导航]] [[开源工具/目录]]
