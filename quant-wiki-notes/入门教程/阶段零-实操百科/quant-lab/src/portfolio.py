from __future__ import annotations

import pandas as pd

from src.momentum import panel_backtest


def load_price_panel(processed_dir, symbols: list[str]) -> pd.DataFrame:
    """Load close panel from quant-lab processed OHLCV files."""
    from pathlib import Path

    from src.data_loader import load_processed_ohlcv

    processed_dir = Path(processed_dir)
    series = {}
    for sym in symbols:
        path = processed_dir / f"{sym}_ohlcv.csv"
        if not path.exists():
            continue
        df = load_processed_ohlcv(path)
        series[sym] = df.set_index("date")["close"].astype(float)
    if not series:
        raise FileNotFoundError("no processed OHLCV for symbols")
    return pd.DataFrame(series).sort_index().dropna(how="all")


def equal_weight_rebalance(
    prices: pd.DataFrame,
    rebalance: str = "ME",
    max_weight: float | None = None,
) -> pd.DataFrame:
    """
    Equal-weight among names with non-NaN price on each rebalance date.
    Weights forward-filled, then shifted 1 day (trade next bar).
    max_weight: optional cap per name (renormalize after cap).
    """
    prices = prices.apply(pd.to_numeric, errors="coerce").sort_index()
    marks = prices.resample(rebalance).last()
    weights = pd.DataFrame(0.0, index=marks.index, columns=prices.columns)
    for dt, row in marks.iterrows():
        avail = row.dropna().index.tolist()
        if not avail:
            continue
        w = 1.0 / len(avail)
        for sym in avail:
            weights.loc[dt, sym] = w
        if max_weight is not None and max_weight > 0:
            weights.loc[dt] = _cap_and_renorm(weights.loc[dt], max_weight)
    daily = weights.reindex(prices.index).ffill().fillna(0.0)
    return daily.shift(1).fillna(0.0)


def _cap_and_renorm(w: pd.Series, max_weight: float) -> pd.Series:
    x = w.clip(upper=max_weight)
    s = x.sum()
    if s <= 0:
        return x
    # If cap left cash, keep residual as cash (weights sum < 1)
    # Optionally renormalize to fully invested — teaching default: renormalize
    return x / s


def inverse_vol_weights(
    prices: pd.DataFrame,
    vol_lookback: int = 20,
    rebalance: str = "ME",
    max_weight: float | None = 0.4,
) -> pd.DataFrame:
    """Risk-budget style toy: weight ∝ 1/vol among available names each rebalance."""
    prices = prices.apply(pd.to_numeric, errors="coerce").sort_index()
    rets = prices.pct_change()
    vol = rets.rolling(vol_lookback).std()
    marks = vol.resample(rebalance).last()
    weights = pd.DataFrame(0.0, index=marks.index, columns=prices.columns)
    for dt, row in marks.iterrows():
        v = row.dropna()
        v = v[v > 0]
        if v.empty:
            continue
        inv = 1.0 / v
        w = inv / inv.sum()
        if max_weight is not None:
            w = _cap_and_renorm(w, max_weight)
        for sym, val in w.items():
            weights.loc[dt, sym] = float(val)
    daily = weights.reindex(prices.index).ffill().fillna(0.0)
    return daily.shift(1).fillna(0.0)


def portfolio_summary(bt: pd.DataFrame) -> dict:
    from src.backtest_simple import summarize

    fake = pd.DataFrame({"equity": bt["equity"], "buy_hold": bt["buy_hold"]})
    out = summarize(fake)
    out["avg_turnover"] = float(bt["turnover"].mean()) if len(bt) else None
    out["avg_gross_exposure"] = float(bt["gross_exposure"].mean()) if len(bt) else None
    return out


def run_weights_backtest(prices: pd.DataFrame, weights: pd.DataFrame, cost_bps: float = 10.0):
    return panel_backtest(prices, weights, cost_bps=cost_bps)
