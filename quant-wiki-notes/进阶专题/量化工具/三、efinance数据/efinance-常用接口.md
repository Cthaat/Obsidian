---
title: efinance 常用接口
tags: [efinance, API, 股票, 基金, 期货]
created: 2026-06-02
source: /opt/data/investment/kb/doc-sites/efinance-数据/
parent: "[[efinance概览]]"
aliases: []
updated: 2026-06-02
---

# efinance 常用接口

> [!note] API 设计理念
> efinance 的 API 极简统一，核心模块为 `ef.stock`、`ef.fund`、`ef.futures`，每个模块提供相同风格的数据获取方法。

## 一、股票（ef.stock）

### 核心方法

| 方法 | 功能 | 返回字段 |
|------|------|---------|
| `get_quote_history(code)` | 获取历史日K线数据 | 股票名称、股票代码、日期、开盘、收盘、最高、最低、成交量、成交额、振幅、涨跌幅、涨跌额、换手率 |

**示例 — A股**：
```python
import efinance as ef

stock_code = '600519'
df = ef.stock.get_quote_history(stock_code)
# 返回从上市首日（2001-08-27）至今的完整日K线
# 贵州茅台: 4761 行 × 13 列
```

**示例 — 非A股（支持代码和名称）**：
```python
# 美股
ef.stock.get_quote_history('AAPL')   # 苹果，从1984年至今
ef.stock.get_quote_history('TSLA')   # 特斯拉

# 港股
ef.stock.get_quote_history('00700')  # 腾讯
```

### 实时行情

| 方法 | 功能 |
|------|------|
| `get_realtime_quotes()` | 获取全部股票实时行情 |
| `get_realtime_quotes(code)` | 获取指定股票实时行情 |

## 二、基金（ef.fund）

| 方法 | 功能 | 说明 |
|------|------|------|
| `get_quote_history(code)` | 获取基金历史净值数据 | 支持公募基金 |

**示例**：
```python
import efinance as ef

# 招商中证白酒
ef.fund.get_quote_history('161725')
```

## 三、期货（ef.futures）

| 方法 | 功能 | 说明 |
|------|------|------|
| `get_quote_history(code)` | 获取期货历史行情 | 如 `RB888`（螺纹钢） |

**示例**：
```python
import efinance as ef

ef.futures.get_quote_history('RB888')
```

## 四、债券（后续版本）

efinance 文档中预留了 `ef.bond` 模块，在后续版本中加入债券数据支持。

## 五、通用方法

| 方法 | 功能 |
|------|------|
| `ef.__version__` | 查看 efinance 版本 |
| `ef.stock.get_base_info(code)` | 获取股票基本信息 |

## API 使用建议

- **网络限流**：使用过程中若遇到限流、连接超时等网络报错，可尝试 [TickFlow](https://tickflow.org) 作为替代数据源
- **Docker 部署**：生产环境推荐 Docker 方式，环境一致性强
- **多品种获取**：`get_quote_history()` 方法统一了股票/基金/期货的K线获取方式

## 相关笔记
- [[efinance概览]]
- [[efinance-版本演进]]

## 实战掌握清单

> [!tip] 交易者视角
> efinance 常用接口 的学习重点不是记住术语，而是把它放进研究、组合、执行和复盘的闭环。量化工具的价值在于提高数据、研究、回测和执行的可靠性，而不是让复杂代码替代投资判断。

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
