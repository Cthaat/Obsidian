---
title: VnPy框架详解
description: VeighNa开源量化交易平台框架详解，41.1k Star，支持AI量化策略
tags: [量化框架, VnPy, VeighNa, Python, CTP, 实盘交易, AI量化]
source: https://github.com/vnpy/vnpy
created: 2026-06-02
---

# VnPy框架详解

> [!note] 框架概览
> **VeighNa**（原VnPy）是一套基于 Python 的**开源量化交易系统开发框架**，41.1k ⭐，11.8k Fork。自发布以来已成为国内最主流的量化交易平台之一，广泛应用于私募基金、证券公司、期货公司等金融机构。4.0 版本新增 **AI 量化策略模块**。

## 基本信息

| 属性 | 值 |
|------|-----|
| GitHub | [vnpy/vnpy](https://github.com/vnpy/vnpy) |
| Star | 41.1k |
| Fork | 11.8k |
| 最新版本 | 4.4.0（2026-05-14） |
| Python版本 | 3.10+（推荐3.13） |
| 系统 | Windows 11+ / Ubuntu 22.04+ / macOS |
| 协议 | MIT |
| 官网 | [vnpy.com](https://www.vnpy.com) |

## AI-Powered（4.0新增）

> [!important] 4.0核心亮点
> VeighNa 4.0 新增 `vnpy.alpha` 模块，提供**一站式多因子机器学习策略开发、投研和实盘交易解决方案**。设计理念受 [Qlib](https://github.com/microsoft/qlib) 启发。

### alpha 模块架构

| 子模块 | 功能 | 说明 |
|--------|------|------|
| **dataset** | 因子特征工程 | 批量特征计算、Alpha 158因子集 |
| **model** | 预测模型训练 | Lasso / LightGBM / MLP |
| **strategy** | 策略投研开发 | 截面多标的 + 时序单标的 |
| **lab** | 投研流程管理 | 数据→模型→信号→回测完整流程 |
| **notebook** | 量化投研Demo | Jupyter Notebook 示例 |

**内置模型**:
- **Lasso**: L1正则化回归，特征选择
- **LightGBM**: 高效梯度提升决策树
- **MLP**: 多层感知机神经网络

**投研Demo**:
- `download_data_rq`: 基于RQData下载A股数据
- `download_data_xt`: 基于迅投研下载数据
- `research_workflow_lasso`: Lasso回归投研流程
- `research_workflow_lgb`: LightGBM投研流程
- `research_workflow_mlp`: MLP深度学习投研流程

## 交易接口（Gateway）

### 国内市场

| 接口 | 代码 | 支持品种 | 4.0适配 |
|------|------|----------|---------|
| CTP | ctp | 国内期货、期权 | ⬆️ |
| CTP Mini | mini | 国内期货、期权 | ⬆️ |
| CTP证券 | sopt | ETF期权 | ⬆️ |
| 飞马 | femas | 国内期货 | ⬆️ |
| 易盛 | esunny | 国内期货、黄金TD | ⬆️ |
| 中泰XTP | xtp | A股、ETF期权 | ⬆️ |
| 华鑫奇点 | tora | A股、ETF期权 | ⬆️ |
| 顶点HTS | hts | ETF期权 | ⬆️ |
| 顶点飞创 | sec | ETF期权 | ⬆️ |
| 东证OST | ost | A股 | |
| 东方财富EMT | emt | A股 | |
| 飞鼠 | sgit | 黄金TD、期货 | |
| 金仕达黄金 | ksgold | 黄金TD | ⬆️ |
| 利星资管 | lstar | 期货资管 | ⬆️ |
| 融航 | rohon | 期货资管 | ⬆️ |
| 杰宜斯 | jees | 期货资管 | ⬆️ |
| 中汇亿达 | comstar | 银行间市场 | |
| TTS | tts | 国内期货（仿真） | ⬆️ |

### 海外市场

| 接口 | 代码 | 支持品种 | 4.0适配 |
|------|------|----------|---------|
| Interactive Brokers | ib | 海外证券、期货、期权、贵金属 | ⬆️ |
| 易盛9.0外盘 | tap | 海外期货 | ⬆️ |
| 直达期货 | da | 海外期货 | ⬆️ |

### 特殊应用

| 接口 | 代码 | 功能 | 4.0适配 |
|------|------|------|---------|
| RQData行情 | rqdata | 跨市场实时行情 | ⬆️ |
| 迅投研行情 | xt | 跨市场实时行情 | ⬆️ |
| RPC服务 | rpc | 跨进程通讯，分布式架构 | ⬆️ |

## 交易应用（App）

| 应用 | 代码 | 功能 | 4.0适配 |
|------|------|------|---------|
| CTA策略引擎 | cta_strategy | CTA策略运行，细粒度委托控制 | ⬆️ |
| CTA回测 | cta_backtester | GUI策略回测、参数优化 | ⬆️ |
| 价差交易 | spread_trading | 自定义价差，价差算法交易 | ⬆️ |
| 期权交易 | option_master | 期权定价、隐含波动率曲面、希腊值 | ⬆️ |
| 组合策略 | portfolio_strategy | 多合约策略（Alpha、期权套利） | ⬆️ |
| 算法交易 | algo_trading | TWAP / Sniper / Iceberg / BestLimit | ⬆️ |
| 脚本策略 | script_trader | 多标的策略、REPL指令交易 | ⬆️ |
| 本地仿真 | paper_account | 纯本地仿真模拟交易 | ⬆️ |
| K线图表 | chart_wizard | 实时K线显示 | ⬆️ |
| 组合管理 | portfolio_manager | 子账户、盈亏统计 | ⬆️ |
| RPC服务 | rpc_service | 多进程分布式系统 | ⬆️ |
| 数据管理 | data_manager | 数据查看、CSV导入导出 | ⬆️ |
| 行情记录 | data_recorder | Tick/K线录制到数据库 | ⬆️ |
| Excel RTD | excel_rtd | Excel实时数据推送 | ⬆️ |
| 风险管理 | risk_manager | 交易流控、下单限制、前端风控 | ⬆️ |
| Web服务 | web_trader | REST + Websocket Web服务器 | ⬆️ |

## 数据库适配

### SQL类

| 数据库 | 代码 | 特点 |
|--------|------|------|
| SQLite | sqlite | 默认选项，单文件，适合新手 |
| MySQL | mysql | 主流开源RDBMS，可替换TiDB |
| PostgreSQL | postgresql | 功能丰富，支持扩展插件 |

### NoSQL类

| 数据库 | 代码 | 特点 |
|--------|------|------|
| QuestDB | questdb | 高性能列式时序数据库 |
| DolphinDB | dolphindb | 分布式高性能时序数据库 |
| TDengine | taos | 支持SQL的分布式时序数据库 |
| MongoDB | mongodb | 文档式数据库，内置热数据缓存 |

## 数据服务适配

| 数据源 | 代码 | 覆盖品种 |
|--------|------|----------|
| 迅投研 | xt | 股票、期货、期权、基金、债券 |
| 米筐RQData | rqdata | 股票、期货、期权、基金、债券、黄金TD |
| MultiCharts | mcdata | 期货、期货期权 |
| TuShare | tushare | 股票、期货、期权、基金 |
| 万得Wind | wind | 股票、期货、基金、债券 |
| 同花顺iFinD | ifind | 股票、期货、基金、债券 |
| 天勤TQSDK | tqsdk | 期货 |
| 掘金 | gm | 股票 |
| polygon | polygon | 股票、期货、期权 |

## 快速启动

### 方式一：VeighNa Studio（推荐）

下载 [VeighNa Studio-4.4.0](https://download.vnpy.com/veighna_studio-4.4.0.exe)，集成框架 + VeighNa Station管理平台。

### 方式二：脚本运行

```python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp

def main():
    qapp = create_qapp()
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()
    qapp.exec()

if __name__ == "__main__":
    main()
```

## 社区资源

- **官方文档**: [vnpy.com/docs](https://www.vnpy.com/docs/cn/index.html)
- **社区论坛**: [vnpy.com/forum](https://www.vnpy.com/forum/)
- **知乎专栏**: [zhuanlan.zhihu.com/vn-py](http://zhuanlan.zhihu.com/vn-py)
- **QQ群**: 262656087
- **微信交流群**: 扫码添加小助手

## 与其他框架对比

| 特性 | VnPy | Backtrader | Zipline |
|------|------|-----------|---------|
| 定位 | 全功能交易平台 | 回测框架 | 回测框架 |
| 实盘支持 | ✅ 20+接口 | 有限 | 有限 |
| AI模块 | ✅ alpha模块 | ❌ | ❌ |
| GUI | ✅ Qt界面 | ❌ | ❌ |
| 社区规模 | 41.1k⭐ | 14k⭐ | 17k⭐ |
| 国内生态 | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |

## 相关笔记

- [[量化开发资源大全]]
- [[CTP接口对接]]
- [[量化系统架构]]
- [[Python量化环境配置]]
- [[量化策略开发]]
