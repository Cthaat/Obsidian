from __future__ import annotations

import pandas as pd


def quick_check(
    df: pd.DataFrame,
    date_col: str = "date",
    close_col: str = "close",
) -> dict:
    """Minimal OHLCV sanity stats for teaching notebooks/scripts."""
    if df is None or len(df) == 0:
        return {
            "rows": 0,
            "dup_dates": None,
            "na_close": None,
            "max_abs_ret": None,
            "start": None,
            "end": None,
        }

    d = df.copy()
    d[date_col] = pd.to_datetime(d[date_col])
    d = d.sort_values(date_col)
    close = pd.to_numeric(d[close_col], errors="coerce")
    ret = close.pct_change()
    return {
        "rows": int(len(d)),
        "dup_dates": int(d[date_col].duplicated().sum()),
        "na_close": int(close.isna().sum()),
        "max_abs_ret": float(ret.abs().max()) if ret.notna().any() else None,
        "start": str(d[date_col].iloc[0].date()),
        "end": str(d[date_col].iloc[-1].date()),
    }
