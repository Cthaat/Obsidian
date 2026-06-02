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
