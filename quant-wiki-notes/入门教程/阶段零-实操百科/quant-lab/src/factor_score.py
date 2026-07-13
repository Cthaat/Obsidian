from __future__ import annotations

import pandas as pd

from src.momentum import panel_backtest


def _zscore_cs(df: pd.DataFrame) -> pd.DataFrame:
    """Cross-sectional z-score each row; NaN-safe."""
    mu = df.mean(axis=1)
    sd = df.std(axis=1).replace(0, pd.NA)
    return df.sub(mu, axis=0).div(sd, axis=0)


def price_factor_scores(
    prices: pd.DataFrame,
    mom_lookback: int = 20,
    vol_lookback: int = 20,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Teaching factors from prices only (all lagged via shift in weights step):
    - momentum: past return (higher better)
    - low_vol: negative realized vol (higher score = lower vol)
    Returns raw mom, raw vol, and combined equal-weight z-score.
    """
    prices = prices.apply(pd.to_numeric, errors="coerce").sort_index()
    mom = prices / prices.shift(mom_lookback) - 1.0
    vol = prices.pct_change().rolling(vol_lookback).std()
    low_vol_score = -vol
    # combine on dates where both exist
    z_mom = _zscore_cs(mom)
    z_lv = _zscore_cs(low_vol_score)
    combined = (z_mom + z_lv) / 2.0
    return mom, vol, combined


def factor_top_k_weights(
    scores: pd.DataFrame,
    top_k: int = 2,
    rebalance: str = "W",
    max_weight: float | None = None,
) -> pd.DataFrame:
    """At rebalance dates, equal-weight top_k by score; ffill; shift 1 day."""
    scores = scores.sort_index()
    marks = scores.resample(rebalance).last()
    weights = pd.DataFrame(0.0, index=marks.index, columns=scores.columns)
    for dt, row in marks.iterrows():
        s = row.dropna().sort_values(ascending=False)
        picks = list(s.index[:top_k])
        if not picks:
            continue
        w = 1.0 / len(picks)
        for sym in picks:
            weights.loc[dt, sym] = w
        if max_weight is not None and max_weight > 0:
            # cap (usually redundant if equal weight 1/k <= max)
            capped = weights.loc[dt].clip(upper=max_weight)
            total = capped.sum()
            if total > 0:
                weights.loc[dt] = capped / total
    daily = weights.reindex(scores.index).ffill().fillna(0.0)
    return daily.shift(1).fillna(0.0)


def run_factor_backtest(
    prices: pd.DataFrame,
    top_k: int = 2,
    mom_lookback: int = 20,
    vol_lookback: int = 20,
    rebalance: str = "W",
    cost_bps: float = 15.0,
    max_weight: float | None = None,
):
    _, _, combined = price_factor_scores(prices, mom_lookback=mom_lookback, vol_lookback=vol_lookback)
    weights = factor_top_k_weights(
        combined, top_k=top_k, rebalance=rebalance, max_weight=max_weight
    )
    bt = panel_backtest(prices, weights, cost_bps=cost_bps)
    return bt, weights, combined
