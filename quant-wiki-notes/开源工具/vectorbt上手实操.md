---
title: vectorbt上手实操
date: 2026-07-13
tags:
  - 开源工具
  - vectorbt
  - 回测
  - 实操
---

# vectorbt上手实操

> [!note] 核心问题
> [vectorbt](https://github.com/polakowo/vectorbt) 用 **NumPy/Numba 向量化** 高速测试大量参数与资产组合，适合「研究扫描」；不适合当作完整 A 股撮合引擎。文档站点：[vectorbt.dev](https://vectorbt.dev/)。

## 学习目标

1. 说清向量化回测与事件驱动的差异。  
2. 完成 `pip install vectorbt` 级安装。  
3. 理解 signals → Portfolio 的基本流水线。  
4. 知道参数广播扫参的用途与过拟合风险。  
5. 与 quant-lab / Backtrader 分工清楚。  

## 它是什么

| 维度 | 说明 |
|---|---|
| 定位 | 高性能向量化回测与组合分析（社区版；另有 PRO） |
| 优势 | 同一套逻辑扫成千上万参数组合极快 |
| 代价 | 路径依赖订单、复杂 A 股规则需自建 |
| 安装 | `pip install -U vectorbt`；可选 `full` / `rust` extra（见官方） |

## 谁该用

| 适合 | 不适合优先 |
|---|---|
| 已有 pandas 基础，要做参数敏感扫描 | 第一周学交易系统 |
| 多资产信号矩阵研究 | 需要逐笔订单仿真 |
| 快速否决劣参数 | 假装已含涨跌停/T+1 |

## 最小心智模型

```text
价格矩阵 (时间 × 资产)
  → 指标 / 信号 (布尔进出场)
  → Portfolio.from_signals(...)  # 名称以当前文档为准
  → stats / plot / trades
```

教学思想（**非保证可运行粘贴**，以 [vectorbt.dev](https://vectorbt.dev/) 示例为准）：

```python
# 伪代码结构
# data = ...  # close series/frame
# fast, slow = ...
# entries = fast_ma > slow_ma
# exits = fast_ma < slow_ma
# pf = vbt.Portfolio.from_signals(data, entries, exits, fees=0.001)
# print(pf.total_return())
```

## 第一小时

| 分钟 | 动作 |
|---:|---|
| 0–10 | 打开 GitHub + vectorbt.dev 示例页 |
| 10–25 | 独立 venv：`pip install -U vectorbt pandas` |
| 25–50 | 复制官方最小示例跑通 |
| 50–60 | 只改 fees 或均线窗口，记录差异 |

## 与其它工具

| 工具 | 关系 |
|---|---|
| quant-lab 向量化脚本 | 更简教学；vectorbt 更强扫参 |
| Backtrader | 事件驱动、订单逻辑 |
| vn.py | 交易系统 |
| Qlib | ML 研究工作流 |

## 常见误区

| 误区 | 更好的理解 |
|---|---|
| 扫参最快=最好策略 | 过拟合工厂 |
| fees=0 | 自欺 |
| 可直接 A 股实盘 | 规则与接口另建 |

## 练习

写 EXP：同一双均线在 quant-lab 与 vectorbt（若跑通）结论是否同向；不同则查成交假设。

## 相关概念

[[工具实操总导航]] [[回测框架选型与最小示例]] [[开源工具常见坑]] [[过拟合识别与防御]]
