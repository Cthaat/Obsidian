from __future__ import annotations

import pandas as pd


def dual_ma_position(close: pd.Series, fast: int = 5, slow: int = 20) -> pd.Series:
    """Long-only position series: 1 when fast MA > slow MA, held from next bar."""
    close = pd.to_numeric(close, errors="coerce")
    fast_ma = close.rolling(fast).mean()
    slow_ma = close.rolling(slow).mean()
    pos = (fast_ma > slow_ma).astype(float).shift(1).fillna(0.0)
    return pos


def long_only_backtest(
    close: pd.Series,
    pos: pd.Series,
    cost_bps: float = 10.0,
) -> pd.DataFrame:
    """
    Extremely simplified long-only backtest for teaching.
    Does NOT model stamp tax sides, lot size, limit moves, or T+1 path dependence fully.
    """
    close = pd.to_numeric(close, errors="coerce")
    ret = close.pct_change().fillna(0.0)
    pos = pos.astype(float).reindex(close.index).fillna(0.0)
    turn = pos.diff().abs().fillna(pos.abs())
    strat_ret = pos * ret - turn * (cost_bps / 10000.0)
    return pd.DataFrame(
        {
            "close": close,
            "pos": pos,
            "ret": ret,
            "strat_ret": strat_ret,
            "equity": (1.0 + strat_ret).cumprod(),
            "buy_hold": (1.0 + ret).cumprod(),
        }
    )


def summarize(bt: pd.DataFrame) -> dict:
    if bt is None or len(bt) == 0:
        return {"total_return": None, "max_drawdown": None, "n_days": 0}
    equity = bt["equity"]
    dd = equity / equity.cummax() - 1.0
    return {
        "total_return": float(equity.iloc[-1] - 1.0),
        "max_drawdown": float(dd.min()),
        "buy_hold_return": float(bt["buy_hold"].iloc[-1] - 1.0),
        "n_days": int(len(bt)),
    }
