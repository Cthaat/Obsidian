from __future__ import annotations

from pathlib import Path

import pandas as pd

# Common Chinese column names from AKShare stock_zh_a_hist (may vary by version).
_RENAME = {
    "日期": "date",
    "开盘": "open",
    "收盘": "close",
    "最高": "high",
    "最低": "low",
    "成交量": "volume",
    "成交额": "amount",
}


def normalize_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Map common CN headers to date/open/high/low/close/volume and clean."""
    out = df.rename(columns={k: v for k, v in _RENAME.items() if k in df.columns}).copy()
    # already-English columns pass through
    lower_map = {c: c.lower() for c in out.columns if c.lower() in {"date", "open", "high", "low", "close", "volume"}}
    out = out.rename(columns=lower_map)

    if "date" not in out.columns:
        raise ValueError(f"No date column after normalize. columns={list(out.columns)}")
    if "close" not in out.columns:
        raise ValueError(f"No close column after normalize. columns={list(out.columns)}")

    out["date"] = pd.to_datetime(out["date"])
    for col in ("open", "high", "low", "close", "volume"):
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")

    out = out.sort_values("date").drop_duplicates("date")
    cols = [c for c in ["date", "open", "high", "low", "close", "volume"] if c in out.columns]
    return out[cols].reset_index(drop=True)


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_processed_ohlcv(path: Path | str) -> pd.DataFrame:
    path = Path(path)
    df = pd.read_csv(path)
    return normalize_ohlcv(df)
