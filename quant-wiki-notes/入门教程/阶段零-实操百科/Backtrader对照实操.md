---
title: Backtrader对照实操
date: 2026-07-13
tags:
  - 投资
  - 量化
  - Backtrader
  - 回测
  - 实操
---

# Backtrader对照实操

> [!note] 核心问题
> 你已经在 [[quant-lab项目模板]] 里用向量化脚本跑通双均线；本篇把同一套 `processed` CSV 接到 **Backtrader 事件驱动**，对照两种引擎的差异，并指向本库可运行代码 `阶段零-实操百科/quant-lab/`。

## 学习目标

读完这篇，你要能做到：

1. 安装 backtrader 并用 quant-lab 脚本跑通一次事件驱动回测。  
2. 说明向量化 `shift(1)` 与 `CrossOver`+`next()` 在成交时点上的异同。  
3. 会设置 cash、commission、stake，并读懂输出 JSON。  
4. 知道 Backtrader 默认仍未自动实现完整 A 股规则。  
5. 在 EXP 笔记中同时记录两套引擎的结果差异。  

## 为何要对照跑两遍

| 引擎 | 优点 | 教学风险 |
|---|---|---|
| 向量化 `run_dual_ma.py` | 快、逻辑透明 | 易漏路径依赖与订单细节 |
| Backtrader `run_backtrader_dual_ma.py` | 接近「逐 bar 决策」 | 参数默认仍会美化 A 股 |

两边都赚/都亏不可怕；**两边结论相反**时，优先查成交时点、持仓单位、成本。

## 代码位置

```text
quant-wiki-notes/入门教程/阶段零-实操百科/quant-lab/
  scripts/pull_akshare_example.py
  scripts/run_dual_ma.py
  scripts/run_backtrader_dual_ma.py
  src/bt_dual_ma.py
  strategies/dual_ma_spec.md
  README.md
```

Vault 内相对路径便于点击；运行时请在 **`quant-lab` 根目录** 打开终端。

## 安装

```powershell
cd "路径\quant-wiki-notes\入门教程\阶段零-实操百科\quant-lab"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python check_env.py
```

若 `backtrader` 未装成功：

```powershell
pip install backtrader
```

绘图可选：`pip install backtrader[plotting]`（依赖较重，教学非必须）。

## 三步跑通

### 1. 准备数据

```powershell
python scripts/pull_akshare_example.py --symbol 000001
```

检查：

- `data/processed/000001_ohlcv.csv`  
- `data/processed/000001_ohlcv.meta.json` 中的 `adjust`  

### 2. 向量化基线

```powershell
python scripts/run_dual_ma.py --symbol 000001 --fast 5 --slow 20 --cost-bps 10
```

输出：`reports/dual_ma_000001_5_20.json`。

### 3. Backtrader

```powershell
python scripts/run_backtrader_dual_ma.py --symbol 000001 --fast 5 --slow 20
```

输出：`reports/bt_dual_ma_000001_5_20.json`。

## 策略逻辑（事件驱动）

`src/bt_dual_ma.py` 核心思想：

```text
fast_ma = SMA(fast)
slow_ma = SMA(slow)
crossover = CrossOver(fast, slow)
next():
  无仓且 crossover > 0 → buy
  有仓且 crossover < 0 → close
```

对照向量化：

```text
pos = (fast_ma > slow_ma).shift(1)
```

| 点 | 向量化 | Backtrader 本实现 |
|---|---|---|
| 金叉判定 | 均线大小关系 | `CrossOver` 由下向上穿越 |
| 持仓 | 0/1 序列 | broker 持仓对象 |
| 仓位量 | 满仓收益近似 | `FixedSize(stake=100)` 默认 100 股 |
| 成本 | 换仓 bps | `commission` 比例近似 |

> [!important]
> 默认 **stake=100** 时，资金利用率与向量化「满仓比例」不同，**收益数字不可直接横比**。要比逻辑，先统一仓位假设（例如加大 stake 或改 sizer），并在笔记写明。

## 关键参数

| 参数 | 脚本开关 | 含义 |
|---|---|---|
| fast/slow | `--fast --slow` | 均线周期 |
| cash | `--cash` | 初始资金（默认 1e5 假设） |
| commission | `--commission` | 比例佣金示意（默认 0.0003） |
| stake | `--stake` | 每次下单股数 |

A 股完整费用、印花税、涨跌停：**未**在脚本中完整建模。见 [[A股交易规则实操要点]]。

## 如何读 JSON 结果

| 字段 | 含义 |
|---|---|
| `start_value` / `end_value` | 期初/期末权益 |
| `total_return` | 简单区间收益 |
| `max_drawdown` | 分析器回撤（实现里按百分数转小数） |
| `engine` | `backtrader` |
| `disclaimer` | 教学限制声明 |

把 JSON 摘要粘贴到 EXP 笔记，勿只截图曲线。

## 与进阶文的关系

| 文档 | 分工 |
|---|---|
| 本篇 | quant-lab 对照实操、命令级 |
| [[Backtrader实战入门]] | 组件更全的教程摘录 |
| [[回测框架选型与最小示例]] | 框架选型 |
| [[开源回测框架全景对比]] | 多框架地图 |
| [[回测方法论]] | 偏差与样本外 |

## 常见报错

| 现象 | 处理 |
|---|---|
| missing processed csv | 先 pull |
| No module named backtrader | pip 安装 |
| 列缺失 open/high/... | 检查 normalize 是否成功，打开 csv 头 |
| 交易次数为 0 | 拉长区间或改参数；检查数据是否过短 |
| 结果与向量化差很多 | 先比 stake/成本，再比交叉定义 |

## 建议实验（一变量）

| 版本 | 唯一变化 |
|---|---|
| v0.1 | 默认 5/20 |
| v0.2 | 仅改 10/30 |
| v0.3 | 仅改 commission 或 cost_bps |
| v0.4 | 仅改 stake |

纪律见 [[研究笔记与实验工作流]]。

## 练习：对照表

| 项目 | 向量化 | Backtrader |
|---|---|---|
| 命令 |  |  |
| 区间 |  |  |
| 参数 |  |  |
| 收益 |  |  |
| 最大回撤 |  |  |
| 仓位假设是否一致 |  |  |
| 差异解释 |  |  |

## 相关概念

[[quant-lab项目模板]] [[回测框架选型与最小示例]] [[Backtrader实战入门]] [[第一个可回测策略]] [[A股交易规则实操要点]]
