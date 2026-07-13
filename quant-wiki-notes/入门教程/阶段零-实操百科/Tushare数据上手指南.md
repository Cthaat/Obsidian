---
title: Tushare数据上手指南
date: 2026-07-13
tags:
  - 投资
  - 量化
  - 数据
  - Tushare
  - 实操
---

# Tushare数据上手指南

> [!note] 核心问题
> [Tushare Pro](https://www.tushare.pro/) 是国内量化常用的数据社区/接口服务：基础可用，进阶靠**积分与权限**。本篇教你注册、存 token、初始化、拉日线与股票列表，并做好权限与安全习惯。具体积分表与接口清单以官网文档为准。

## 学习目标

读完这篇，你要能做到：

1. 注册并取得 token，用环境变量注入而非写死在代码库。
2. 安装 `tushare` 并初始化 `pro_api`。
3. 拉取股票列表与日线行情，理解 `ts_code` 与交易日期格式。
4. 知道权限不足时如何读文档，而不是盲目重试。
5. 与 AKShare 形成「主源 + 抽查源」组合。

## Tushare 是什么（定位）

| 维度 | 说明 |
|---|---|
| 定位 | 面向量化与研究的数据接口社区（Pro） |
| 与旧版 | 早期开源 Org 版与 Pro 不同；新项目用 Pro 文档 |
| 费用逻辑 | 普通用户保有基础数据路径；更高频次/更多接口常需积分或套餐 |
| 适用 | 本地研究、财务与行情字段、教学作品集 |
| 不适用预期 | 不保证零运维的机构级实时交易主源 |

官方介绍强调标准化治理与社区，并提供 Python 等 SDK；积分与频次见官网「积分频次」类说明。

深读工程风控视角：[[TuShare数据接口]]（进阶专题偏运维清单）。选型对比：[[数据源全景与选型]]。

## 一、注册与 token

### 步骤（对照官网操作手册）

文档入口：https://tushare.pro/document/1  

1. 完成**用户注册**（见文档「操作手册 → 用户注册」）。  
2. **获取 token**（见文档「获取 token」）。  
3. 打开 **权限中心** 了解积分与频次：https://tushare.pro/weborder/#/permission  
4. 调接口前先看该接口的积分要求与「积分频次表」（文档内链）。  
5. （可选）社区 QQ/公众号等支持渠道以官网公示为准。  

### 安全规则

| 做 | 不做 |
|---|---|
| 用环境变量 `TUSHARE_TOKEN` | 把 token 提交到 GitHub |
| 本地 `.env` 并加入 `.gitignore` | 把 token 发到公开群 |
| 泄露后立即重置 | 多台机器共用截图明文 |

#### Windows PowerShell 临时设置

```powershell
$env:TUSHARE_TOKEN = "你的token"
```

#### 长期（用户环境变量）

系统设置 → 环境变量 → 新建用户变量 `TUSHARE_TOKEN`。或使用 `python-dotenv` 加载本地 `.env`（勿提交）。

## 二、安装与初始化

```powershell
pip install tushare pandas
# 或
pip install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple
```

```python
import os
import tushare as ts
import pandas as pd

token = os.environ.get("TUSHARE_TOKEN")
if not token:
    raise RuntimeError("请先设置环境变量 TUSHARE_TOKEN")

pro = ts.pro_api(token)
# 部分环境也可: ts.set_token(token); pro = ts.pro_api()
print("Tushare pro ready")
```

> [!tip]
> 安装后若接口行为异常，先 `pip install -U tushare`，并查看官网更新日志。

## 三、核心概念

| 概念 | 含义 | 注意 |
|---|---|---|
| `ts_code` | 如 `000001.SZ`、`600000.SH` | 与聚宽等平台代码规则不同 |
| `trade_date` | 常为 `YYYYMMDD` 字符串 | 不是 datetime 对象 |
| 积分/权限 | 接口级门槛 | 报错时先查该接口权限说明 |
| 频次 | 单位时间调用次数 | 循环拉全市场要限速与缓存 |
| 复权 | 日线复权接口或因子字段 | 以文档字段为准，笔记写明 |

## 四、最小可用示例

> 下列接口名与字段为**社区常用形态示意**。若你的权限或版本不同，以 [Tushare 文档](https://tushare.pro/document/2) 当前页面为准。

### 1. 股票基础列表

```python
# 示意：股票列表
# stock_basic = pro.stock_basic(
#     exchange="",
#     list_status="L",
#     fields="ts_code,symbol,name,area,industry,list_date",
# )
# print(stock_basic.head())
```

用途：构建股票池宇宙、排除退市（`list_status` 等字段含义见文档）。

### 2. 日线行情

```python
# 示意：日线
# df = pro.daily(ts_code="000001.SZ", start_date="20200101", end_date="20231231")
# print(df.tail())
```

常见字段思想：开高低收、成交量额、涨跌幅等。是否复权、复权因子是否在另一接口，**必须读该接口文档**。

### 3. 交易日历

```python
# 示意
# cal = pro.trade_cal(exchange="SSE", start_date="20200101", end_date="20201231")
```

用途：对齐回测日历、避免把周末当缺失乱填。

### 4. 保存与元数据

```python
from pathlib import Path
from datetime import datetime

out = Path("data/raw")
out.mkdir(parents=True, exist_ok=True)

# df.to_csv(out / "000001_SZ_daily.csv", index=False)
meta = {
    "source": "tushare",
    "api": "daily",
    "ts_code": "000001.SZ",
    "pulled_at": datetime.now().isoformat(timespec="seconds"),
}
# 把 meta 写到同名 .json 或研究笔记
print(meta)
```

## 五、权限不足时怎么办

| 步骤 | 动作 |
|---:|---|
| 1 | 复制完整报错信息 |
| 2 | 打开该接口文档，看「积分要求/权限」 |
| 3 | 检查是否 token 未生效、套餐未到账 |
| 4 | 换**低权限**等价接口做学习（或先用 AKShare） |
| 5 | 需要再计划积分获取，避免无目的刷接口 |

> [!important]
> 不要用多账号绕过服务条款。学习阶段用 AKShare 补齐缺口完全合理。

## 六、与 AKShare 如何搭配

| 场景 | 建议 |
|---|---|
| 第一次课 | AKShare 无 token 压力 |
| 需要稳定字段/财务 | Tushare 按权限使用 |
| 交叉验证 | 同一日收盘价两源抽查 |
| 全市场每日更新 | 缓存 + 限速 + 断点续传 |

见 [[数据源全景与选型]]、[[AKShare概览]]。

## 七、全市场拉取的纪律

```text
错误：for code in all_stocks: pro.daily(code)  # 易触发频次墙且难维护
更好：
  - 只拉你股票池
  - 按 trade_date 增量更新
  - 本地 CSV/Parquet/SQLite 落盘
  - 失败重试有上限与日志
```

教学阶段**不要**一上来同步全 A 分钟线。

## 八、质量检查（拉完必做）

沿用 [[数据源全景与选型]] 的检查表，并加两条：

| 检查 | 说明 |
|---|---|
| `ts_code` 一致性 | 文件名与列一致 |
| 权限样本 | 记录「当前积分档位能用的接口清单」 |

## 九、常见误区

| 误区 | 更好的理解 |
|---|---|
| 有 token 就能打尽所有接口 | 接口级权限不同 |
| token 写进 Notebook 就分享 | 先脱敏 |
| 不落盘每次重拉 | 浪费频次且不可复现 |
| 忽略 trade_date 格式 | 是最常见空表原因之一 |
| 用 Tushare 替代交易行情主源实盘 | 实盘许可与延迟另议 |

## 练习：Tushare 验收

| 项 | 你的结果 |
|---|---|
| token 是否仅存在环境变量 |  |
| `pro` 初始化成功 |  |
| 成功接口 1（名称） |  |
| 成功接口 2（名称） |  |
| 数据保存路径 |  |
| 与 AKShare 抽查是否一致 |  |

## 相关概念

[[数据源全景与选型]] [[Python量化环境搭建]] [[TuShare数据接口]] [[复权与公司行动实操]] [[研究笔记与实验工作流]] [[全库网络资源总表]]
