---
title: EasyQuant 后端架构
tags: [EasyQuant, FastAPI, SQLAlchemy, 数据库, 回测引擎]
created: 2026-06-02
source: /opt/data/investment/kb/repos/EasyQuant/web_strategy_studio/backend/
parent: "[[EasyQuant概览]]"
aliases: []
updated: 2026-06-02
---

# EasyQuant 后端架构

> [!note] 概述
> EasyQuant Web Studio 后端基于 FastAPI，使用 SQLAlchemy 2 异步模式 + SQLite 存储，通过子进程隔离执行回测任务。

## 数据模型

### User（用户）

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | String(64) | 主键 |
| `username` | String(256) | 用户名，唯一 |
| `hashed_password` | Text | 密码哈希 |
| `is_active` | bool | 是否激活，默认 True |
| `created_at` | DateTime | 创建时间 |

### Strategy（策略）

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | String(64) | 主键，格式 `strat_{hex}` |
| `owner_id` | FK → User | 所有者 |
| `name` | Text | 策略名称 |
| `description` | Text | 策略描述 |
| `current_version` | Integer | 当前版本号 |
| `default_params` | JSON | 默认回测参数 |
| `created_at` / `updated_at` | DateTime | 时间戳 |

### StrategyVersion（策略版本）

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | String(64) | 主键 |
| `strategy_id` | FK → Strategy | 所属策略 |
| `version` | Integer | 版本号 |
| `source_code` | Text | 策略源码 |
| `content_hash` | String(64) | SHA256 内容哈希（去重） |
| `label` | String(256) | 快照标签 |

### Run（回测记录）

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | String(64) | 主键 |
| `strategy_id` | FK → Strategy | 所属策略 |
| `status` | String(32) | 状态：queued/running/completed/failed |
| `progress` | Float | 进度百分比 |
| `params` | JSON | 回测参数 |
| `html_path` / `json_path` | Text | 报告产物路径 |
| `error_code` / `error_message` | Text | 错误信息 |
| `started_at` / `finished_at` | DateTime | 时间 |

## 回测执行流程

```
用户提交回测
  → POST /api/v1/runs (status=queued)
  → RunQueue 从队列取任务
  → IsolatedRunner 创建子进程
  → 子进程执行: run_backtest() → generate_html_report()
  → SSE 推送进度 (RunProgressBar)
  → 结果存入 artifacts/
  → Run 状态更新为 completed/failed
```

## 关键组件

| 组件 | 文件 | 功能 |
|------|------|------|
| Runner 协议 | `runner.py` | 抽象回测执行接口（Local + Docker） |
| 隔离执行器 | `isolated_runner.py` | 子进程隔离执行策略代码 |
| 进程注册表 | `proc_registry.py` | 跟踪运行中的子进程，支持取消 |
| 运行队列 | `run_queue.py` | 管理回测任务队列 |
| 流中心 | `stream_hub.py` | SSE 流事件分发 |
| 代码检查 | `lint_service.py` | Python 代码静态检查 |
| 安全扫描 | `security_scanner.py` | 策略源码安全扫描 |

## Runner 安全机制

- **LocalRunner**：不提供沙箱，仅限受信任单机使用（API 绑定 `127.0.0.1`）
- **DockerRunner**：容器内执行：`--network none --read-only --tmpfs /tmp --memory=2g --pids-limit=64 --security-opt no-new-privileges`
- 环境变量过滤：阻断 `EQ_JWT_SECRET`、`EQ_ADMIN_PASSWORD`、`EQ_STUDIO_DATABASE_URL` 等敏感变量

## 数据库迁移

使用 Alembic 进行数据库版本管理：

```
backend/
├── alembic.ini
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── 0001_init.py
```

## 测试覆盖

| 测试文件 | 覆盖内容 |
|---------|---------|
| `test_auth.py` | 用户认证 |
| `test_runner_isolation.py` | 执行隔离 |
| `test_rate_limit.py` | 频率限制 |
| `test_optimistic_lock.py` | 乐观锁 |
| `test_orphan_cleanup.py` | 孤儿记录清理 |
| `test_path_traversal.py` | 路径穿越防护 |
| `test_report_access_control.py` | 报告访问控制 |
| `test_report_xss.py` | XSS 防护 |
| `test_strategy_versions.py` | 策略版本管理 |
| `test_runs_queue.py` | 运行队列 |
| `test_stream_hub_replay.py` | SSE 流重放 |

## 相关笔记
- [[EasyQuant概览]]
- [[EasyQuant-Web策略工作室]]
- [[EasyQuant-教程体系]]

## 实战掌握清单

> [!tip] 交易者视角
> EasyQuant 后端架构 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

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
