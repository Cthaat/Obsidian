---
title: quant-lab项目模板
date: 2026-07-13
tags:
  - 投资
  - 量化
  - Python
  - 实操
  - 工程
---

# quant-lab项目模板

> [!note] 核心问题
> 环境装好了仍会乱：数据、Notebook、策略、报告搅在一起就无法复现。本篇给出一个**最小可复制的 quant-lab 目录与模板代码**，对应 [[Python量化环境搭建]] 与 [[研究笔记与实验工作流]]。

## 学习目标

读完这篇，你要能做到：

1. 按模板建好目录与 `requirements.txt`。  
2. 用脚本拉取并落盘一只股票日线。  
3. 跑通向量化双均线回测示例并导出权益曲线数据。  
4. 理解为何 raw/processed 分离。  
5. 用 README 让「未来的自己」能复现。  

## 目录模板

```text
quant-lab/
  README.md
  requirements.txt
  .gitignore
  check_env.py
  data/
    raw/
    processed/
  notebooks/
  src/
    __init__.py
    config.py
    data_loader.py
    quality.py
    backtest_simple.py
  strategies/
    dual_ma_spec.md
  reports/
  scripts/
    pull_akshare_example.py
    run_dual_ma.py
```

### .gitignore 最小

```text
.venv/
__pycache__/
.env
data/raw/
data/processed/
reports/*.png
.ipynb_checkpoints/
```

> [!tip]
> 若需要复现实验，可选择把**某次** `processed` 样例数据纳入版本库；默认忽略是为了避免巨量 CSV。至少在笔记中保留元数据。

## requirements.txt（学习最小集）

```text
numpy
pandas
matplotlib
akshare
# 可选回测
backtrader
```

安装：

```powershell
cd quant-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## src/config.py

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"

# 教学默认；策略中请显式覆盖
DEFAULT_START = "20200101"
DEFAULT_END = "20231231"
DEFAULT_ADJUST = "qfq"
```

## src/quality.py

```python
import pandas as pd

def quick_check(df: pd.DataFrame, date_col: str = "date", close_col: str = "close") -> dict:
    d = df.copy()
    d[date_col] = pd.to_datetime(d[date_col])
    d = d.sort_values(date_col)
    ret = d[close_col].astype(float).pct_change()
    return {
        "rows": len(d),
        "dup_dates": int(d[date_col].duplicated().sum()),
        "na_close": int(d[close_col].isna().sum()),
        "max_abs_ret": float(ret.abs().max()) if len(d) else None,
        "start": str(d[date_col].iloc[0].date()) if len(d) else None,
        "end": str(d[date_col].iloc[-1].date()) if len(d) else None,
    }
```

## src/data_loader.py

```python
from __future__ import annotations

from pathlib import Path
import pandas as pd

def normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """尽量把中文列名映射到统一英文列（按实际列调整）。"""
    rename = {
        "日期": "date",
        "开盘": "open",
        "收盘": "close",
        "最高": "high",
        "最低": "low",
        "成交量": "volume",
    }
    out = df.rename(columns={k: v for k, v in rename.items() if k in df.columns}).copy()
    out["date"] = pd.to_datetime(out["date"])
    out = out.sort_values("date").drop_duplicates("date")
    cols = [c for c in ["date", "open", "high", "low", "close", "volume"] if c in out.columns]
    return out[cols].reset_index(drop=True)

def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
```

## scripts/pull_akshare_example.py

```python
"""教学示例：拉取 A 股日线。接口以 akshare 当前版本文档为准。"""
from __future__ import annotations

import json
from datetime import datetime

import akshare as ak

from src.config import DATA_RAW, DATA_PROCESSED, DEFAULT_ADJUST, DEFAULT_END, DEFAULT_START
from src.data_loader import normalize_ohlcv, save_csv
from src.quality import quick_check

def main(symbol: str = "000001") -> None:
    # 参数名若有变更，请改官方文档
    raw = ak.stock_zh_a_hist(
        symbol=symbol,
        period="daily",
        start_date=DEFAULT_START,
        end_date=DEFAULT_END,
        adjust=DEFAULT_ADJUST,
    )
    raw_path = DATA_RAW / f"{symbol}_{DEFAULT_ADJUST}_{DEFAULT_START}_{DEFAULT_END}.csv"
    save_csv(raw, raw_path)

    df = normalize_ohlcv(raw)
    proc_path = DATA_PROCESSED / f"{symbol}_ohlcv.csv"
    save_csv(df, proc_path)

    report = quick_check(df)
    meta = {
        "source": "akshare",
        "api": "stock_zh_a_hist",
        "symbol": symbol,
        "adjust": DEFAULT_ADJUST,
        "pulled_at": datetime.now().isoformat(timespec="seconds"),
        "quality": report,
    }
    meta_path = DATA_PROCESSED / f"{symbol}_ohlcv.meta.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(meta)


if __name__ == "__main__":
    main()
```

运行（在 `quant-lab` 根目录）：

```powershell
python -m scripts.pull_akshare_example
# 若包导入路径有问题，可用：
# $env:PYTHONPATH = (Get-Location).Path
# python scripts/pull_akshare_example.py
```

## src/backtest_simple.py

```python
from __future__ import annotations

import pandas as pd

def dual_ma_position(close: pd.Series, fast: int = 5, slow: int = 20) -> pd.Series:
    fast_ma = close.rolling(fast).mean()
    slow_ma = close.rolling(slow).mean()
    # 收盘出信号，下一期持仓，降低前视
    pos = (fast_ma > slow_ma).astype(float).shift(1).fillna(0.0)
    return pos

def long_only_backtest(
    close: pd.Series,
    pos: pd.Series,
    cost_bps: float = 10.0,
) -> pd.DataFrame:
    ret = close.astype(float).pct_change().fillna(0.0)
    turn = pos.diff().abs().fillna(pos.abs())
    strat_ret = pos * ret - turn * (cost_bps / 10000.0)
    out = pd.DataFrame(
        {
            "close": close,
            "pos": pos,
            "ret": ret,
            "strat_ret": strat_ret,
            "equity": (1.0 + strat_ret).cumprod(),
            "buy_hold": (1.0 + ret).cumprod(),
        }
    )
    return out

def summarize(bt: pd.DataFrame) -> dict:
    equity = bt["equity"]
    dd = equity / equity.cummax() - 1.0
    return {
        "total_return": float(equity.iloc[-1] - 1.0) if len(equity) else None,
        "max_drawdown": float(dd.min()) if len(dd) else None,
        "n_days": int(len(bt)),
    }
```

## scripts/run_dual_ma.py

```python
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from src.backtest_simple import dual_ma_position, long_only_backtest, summarize
from src.config import DATA_PROCESSED, REPORTS

def main(symbol: str = "000001", fast: int = 5, slow: int = 20, cost_bps: float = 10.0) -> None:
    path = DATA_PROCESSED / f"{symbol}_ohlcv.csv"
    df = pd.read_csv(path, parse_dates=["date"])
    pos = dual_ma_position(df["close"], fast=fast, slow=slow)
    bt = long_only_backtest(df["close"], pos, cost_bps=cost_bps)
    bt.insert(0, "date", df["date"].values)

    REPORTS.mkdir(parents=True, exist_ok=True)
    out_csv = REPORTS / f"dual_ma_{symbol}_{fast}_{slow}.csv"
    bt.to_csv(out_csv, index=False)

    summary = summarize(bt)
    summary.update({"symbol": symbol, "fast": fast, "slow": slow, "cost_bps": cost_bps})
    (REPORTS / f"dual_ma_{symbol}_{fast}_{slow}.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(summary)


if __name__ == "__main__":
    main()
```

> [!warning]
> 该向量化回测**极度简化**：无印花税分边、无涨跌停、无 100 股手数、无真实撮合。仅用于打通工程闭环。严肃结论请上平台引擎或完善规则，见 [[A股交易规则实操要点]]、[[回测框架选型与最小示例]]。

## strategies/dual_ma_spec.md

用 [[第一个可回测策略]] 的说明书缩略版，至少写：逻辑、参数、费用、区间、失效条件。

## README.md 骨架

```markdown
# quant-lab

## 环境
python -m venv .venv
# activate
pip install -r requirements.txt

## 取数
python scripts/pull_akshare_example.py

## 回测
python scripts/run_dual_ma.py

## 说明
数据口径与复权见 processed 旁 .meta.json
实验笔记见 Obsidian 阶段零 / 实验日志
```

## 与 Backtrader 的衔接

当向量化跑通后：

1. `processed/*_ohlcv.csv` 作为 `GenericCSVData` 输入；  
2. 策略逻辑保持与说明书一致；  
3. 新版本号 `dual_ma_bt_v0.1`。  

见 [[Backtrader实战入门]]。

## 验收清单

- [ ] 目录齐全  
- [ ] `pull` 生成 raw + processed + meta  
- [ ] `quick_check` 无异常天量涨跌（或已知除权已复权）  
- [ ] `run_dual_ma` 输出 csv/json  
- [ ] README 可让自己下周复现  
- [ ] Obsidian 有一条 EXP 笔记链接到 reports  

## 常见误区

| 误区 | 更好的理解 |
|---|---|
| 全部在 Desktop 散落 py | 无根目录即无项目 |
| 策略里直接网拉数据 | 研究不可复现 |
| 不写 meta | 三个月后不知道复权 |
| 一上来微服务化 | 阶段零保持脚本级即可 |

## 练习：建库打卡

| 项 | 路径或结果 |
|---|---|
| 根目录 |  |
| 第一次 pull 的 symbol |  |
| max_abs_ret |  |
| dual_ma total_return（教学） |  |
| 对应 EXP 笔记名 |  |

## 相关概念

[[Python量化环境搭建]] [[研究笔记与实验工作流]] [[第一个可回测策略]] [[数据源全景与选型]] [[复权与公司行动实操]]
