# quant-lab（阶段零可运行实验目录）

教学用最小量化研究工程，配套笔记：

- [[quant-lab项目模板]]
- [[Python量化环境搭建]]
- [[Backtrader对照实操]]
- [[财务数据实操]]
- [[研究笔记与实验工作流]]

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
```

## 一键流程

```powershell
# 1) 拉日线（默认 000001 前复权 2020-2023）
python scripts/pull_akshare_example.py

# 2) 向量化双均线（简化撮合）
python scripts/run_dual_ma.py

# 3) Backtrader 事件驱动（需 backtrader）
python scripts/run_backtrader_dual_ma.py

# 4) 财务表示意拉取（接口因版本而异）
python scripts/pull_financials_example.py --symbol 600519
```

## 输出

| 步骤 | 输出 |
|---|---|
| pull | `data/raw/*.csv`, `data/processed/*_ohlcv.csv`, `*.meta.json` |
| run_dual_ma | `reports/dual_ma_*.csv|json` |
| run_backtrader | `reports/bt_dual_ma_*.json` |
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
