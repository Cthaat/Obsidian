# quant-lab（阶段零可运行实验目录）

教学用最小量化研究工程，配套笔记：

- [[quant-lab项目模板]]
- [[Python量化环境搭建]]
- [[Backtrader对照实操]]
- [[动量策略实操]]
- [[组合层实操]]
- [[因子打分实操]]
- [[模拟盘日志实操]]
- [[阶段一作业打通清单]]
- [[阶段三作业打通清单]]
- [[阶段四风控卡实操]]
- [[财务数据实操]]
- [[研究笔记与实验工作流]]
- [[实验日志目录]]
- [[阶段零完成验收]]
- [[实操百科总索引]]

> 示例数字与结果均为教学用途，**不构成投资建议**。AKShare / Backtrader 接口升级后请以官方文档为准微调。

## 目录

```text
quant-lab/
  check_env.py
  requirements.txt
  src/           # 可导入库
  scripts/       # 命令行入口
  data/raw|processed
  reports/
  strategies/    # 说明书
```

## 环境

在 **本目录**（`quant-lab`）下执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python check_env.py
# 无网络结构自检 + 可选合成回测
python scripts/run_stage0_check.py
python scripts/run_stage0_check.py --with-synthetic-backtest
```

# 一键流程

```powershell
# 1) 拉日线（默认 000001 前复权 2020-2023）
python scripts/pull_akshare_example.py

# 2) 向量化双均线（简化撮合）
python scripts/run_dual_ma.py

# 3) Backtrader 事件驱动（需 backtrader）
python scripts/run_backtrader_dual_ma.py

# 4) 时序动量（第二策略）
python scripts/run_ts_momentum.py --lookback 20

# 5) 观察池截面动量（先 pull_watchlist）
python scripts/pull_watchlist.py
python scripts/run_cross_section_momentum.py

# 6) 组合层：月度等权 / 逆波动
python scripts/run_equal_weight_rebalance.py --scheme equal --rebalance ME
python scripts/run_equal_weight_rebalance.py --scheme inv_vol

# 7) 价量双因子打分 top-k（教学，无财务 PIT）
python scripts/run_factor_score.py --top-k 2

# 8) 模拟盘 CSV 日志（非实盘下单）
python scripts/init_paper_log.py --name dual_ma_000001
python scripts/append_paper_signal.py --name dual_ma_000001 --symbol 000001

# 9) 报告风控摘要（对已有 reports/*.json）
python scripts/summarize_report.py reports/dual_ma_000001_5_20.json --max-dd-limit 0.25

# 10) 财务表示意拉取
python scripts/pull_financials_example.py --symbol 600519
```

## 输出

| 步骤 | 输出 |
|---|---|
| pull | `data/raw/*.csv`, `data/processed/*_ohlcv.csv`, `*.meta.json` |
| run_dual_ma | `reports/dual_ma_*.csv|json` |
| run_backtrader | `reports/bt_dual_ma_*.json` |
| ts momentum | `reports/ts_mom_*.json` |
| xs momentum | `reports/xs_mom_*.json` |
| portfolio | `reports/port_*.json` |
| factor score | `reports/factor_*.json` |
| paper log | `data/paper_logs/*.csv` |
| summarize | 终端 flags；可选 `--json-out` |
| financials | `data/processed/*_financials.meta.json` 与成功的表 |

## 重要限制

1. 简化回测 **不等于** 可实盘；见 [[A股交易规则实操要点]]。  
2. 财务脚本只保证「尽量拉到表」，字段映射与 PIT 需你按 [[财务数据实操]] 处理。  
3. 不要把 token 或实盘密钥放进本目录后提交 git。  

## 与 Obsidian 的关系

| 你在 Vault 写 | 本目录放 |
|---|---|
| EXP 实验笔记 | `reports/` 结果与 `strategies/*_spec.md` |
| 复权结论 | `*.meta.json` 的 `adjust` 字段 |
| 否决库 | 失败实验的 json 摘要 |
