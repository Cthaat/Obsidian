---
title: EasyQuant Web 策略工作室
tags: [EasyQuant, Web Studio, 策略编辑, Monaco, React]
created: 2026-06-02
source: /opt/data/investment/kb/repos/EasyQuant/web_strategy_studio/
parent: "[[EasyQuant概览]]"
aliases: []
updated: 2026-06-02
---

# EasyQuant Web 策略工作室

> [!note] 概述
> **Web 策略工作室（Web Strategy Studio）** 是 EasyQuant 的前端界面，让用户在浏览器中编写基于 `eqlib` 的 Python 策略、运行静态检查、异步回测，并通过 SSE 查看日志与进度。

## 技术架构

| 组件 | 技术 | 说明 |
|------|------|------|
| 后端 | FastAPI + SQLAlchemy 2 (async) + SQLite | REST `/api/v1/*`、SSE 流、用户认证 |
| 前端 | React 18 + TypeScript + Vite + Monaco | 70/30 布局、设计 token 对齐 HTML 报告 |
| 执行层 | `asyncio` 子进程 + 隔离执行器 | MVP 进程内队列；可替换为 Redis Worker |

## 环境要求

- **Python** 3.9+（推荐 3.11）
- **Node** 18+（推荐 20 LTS）
- 已安装 `eqlib`：`pip install -e .`

## 环境变量（后端）

所有变量以 `EQ_STUDIO_` 为前缀：

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `EQ_STUDIO_DATABASE_URL` | SQLAlchemy 异步 DSN | `sqlite+aiosqlite:///./studio.sqlite3` |
| `EQ_STUDIO_ARTIFACT_DIR` | 报告与产物根目录 | `./artifacts` |
| `EQ_STUDIO_RUN_TIMEOUT_SEC` | 单任务墙钟超时 | `900` (秒) |
| `EQ_STUDIO_MAX_MEMORY_MB` | 内存限制（预留） | `2048` |
| `EQ_STUDIO_REPO_ROOT` | eqlib 仓库根路径 | 自动解析 |
| `EQ_STUDIO_UVICORN_PORT` | uvicorn 监听端口 | `8080` |

## 本地开发

### 一条命令启动（推荐）

```bash
cd web_strategy_studio
npm run install:all
npm run dev:all
# 后端: http://127.0.0.1:8080
# 前端: http://localhost:5173
```

### Docker 部署

```bash
docker-compose up -d
```

## 前端组件架构

| 组件 | 功能 |
|------|------|
| `AppShell.tsx` | 应用壳框架 |
| `MonacoStrategyEditor.tsx` | Monaco 编辑器（Python 高亮 + eqlib 自动补全） |
| `Sidebar.tsx` | 侧边栏导航 |
| `StrategyLayout.tsx` | 70/30 主布局 |
| `RunProgressBar.tsx` | 回测进度条（SSE 实时更新） |
| `ReportViewer.tsx` | HTML 报告查看器 |
| `RunsHistoryPanel.tsx` | 历史回测记录面板 |
| `DataManagementPanel.tsx` | 数据管理面板 |
| `StockPicker.tsx` | 股票代码选择器 |
| `MetricsComparison.tsx` | 策略指标对比 |
| `LogConsole.tsx` | 日志控制台 |
| `CommandPalette.tsx` | 命令面板（键盘快捷键） |

## 后端 API 架构

| 路由模块 | 端点前缀 | 功能 |
|---------|---------|------|
| `auth.py` | `/api/v1/auth` | 用户认证（JWT） |
| `strategies.py` | `/api/v1/strategies` | 策略 CRUD + 版本管理 |
| `runs.py` | `/api/v1/runs` | 回测运行管理 + SSE 流 |
| `completion.py` | `/api/v1/completion` | eqlib 代码自动补全 |
| `lint.py` | `/api/v1/lint` | Python 代码静态检查 |
| `format.py` | `/api/v1/format` | 代码格式化 |
| `data_mgmt.py` | `/api/v1/data` | 数据下载与管理 |
| `symbols.py` | `/api/v1/symbols` | 股票代码搜索 |
| `health.py` | `/api/v1/health` | 健康检查 |

## 默认策略模板

Web Studio 内置**双均线策略模板**：

```python
"""EasyQuant 均线交叉策略 — 在 Web Studio 中编辑并运行回测."""
from eqlib import *

def initialize(context):
    g.security = "601390"
    g.fast_period = 5
    g.slow_period = 20

    set_benchmark("000300.XSHG")
    set_order_cost(OrderCost(
        open_tax=0, close_tax=0.001,
        open_commission=0.0003, close_commission=0.0003,
        close_today_commission=0, min_commission=5,
    ))

    context.universe = [g.security]
    run_daily(market_open, time="every_bar")

def market_open(context):
    # 金叉买入，死叉卖出
    security = g.security
    close_data = attribute_history(security, 25, "1d", ["close"])
    fast_ma = close_data["close"].tail(g.fast_period).mean()
    slow_ma = close_data["close"].tail(g.slow_period).mean()
    # ... 交易逻辑
```

## 隔离执行与安全

| 机制 | 说明 |
|------|------|
| 子进程执行 | 策略代码在独立子进程中运行 |
| 环境变量过滤 | 阻断敏感变量（JWT_SECRET、数据库URL等） |
| `proc_registry` | 进程注册表，支持取消正在运行的策略 |
| `isolated_runner` | 隔离执行器，调用 `run_backtest` 与 `generate_html_report` |

## 相关笔记
- [[EasyQuant概览]]
- [[EasyQuant-后端架构]]
- [[EasyQuant-教程体系]]

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
