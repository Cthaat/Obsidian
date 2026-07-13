from __future__ import annotations

import pandas as pd


def ts_momentum_position(
    close: pd.Series,
    lookback: int = 20,
    skip: int = 0,
) -> pd.Series:
    """
    Time-series momentum (long/flat): hold if past lookback return > 0.
    skip: optionally skip most recent `skip` days when measuring formation return
          (common in research to avoid short-term reversal; 0 keeps it simple).
    Position is shifted by 1 bar (signal at close, hold next bar).
    """
    close = pd.to_numeric(close, errors="coerce")
    if skip < 0:
        raise ValueError("skip must be >= 0")
    if lookback < 1:
        raise ValueError("lookback must be >= 1")

    # Formation return ending `skip` bars ago over `lookback` bars.
    end = close.shift(skip)
    start = close.shift(skip + lookback)
    formation = end / start - 1.0
    raw = (formation > 0).astype(float)
    return raw.shift(1).fillna(0.0)


def apply_max_dd_halt(
    pos: pd.Series,
    close: pd.Series,
    max_dd: float = 0.2,
    cost_bps: float = 10.0,
) -> pd.Series:
    """
    Simple path-dependent risk overlay for teaching:
    while strategy equity drawdown from peak exceeds max_dd, force flat.
    Re-enable after drawdown recovers within half the threshold (simple hysteresis).
    """
    # Bar loop for teaching clarity (not optimized).
    close = pd.to_numeric(close, errors="coerce")
    pos = pos.astype(float).reindex(close.index).fillna(0.0)
    ret = close.pct_change().fillna(0.0)
    out = pos.copy()
    equity = 1.0
    peak = 1.0
    halted = False
    prev_pos = 0.0
    for i in range(len(close)):
        p = 0.0 if halted else float(pos.iloc[i])
        turn = abs(p - prev_pos)
        r = p * float(ret.iloc[i]) - turn * (cost_bps / 10000.0)
        equity *= 1.0 + r
        peak = max(peak, equity)
        dd = equity / peak - 1.0
        if dd <= -abs(max_dd):
            halted = True
        # recover when back within half of max_dd (simple)
        if halted and dd > -abs(max_dd) * 0.5:
            halted = False
        out.iloc[i] = 0.0 if halted else p
        prev_pos = float(out.iloc[i])
    return out


def cross_section_weights(
    price_panel: pd.DataFrame,
    lookback: int = 20,
    top_k: int = 2,
    rebalance: str = "W",
) -> pd.DataFrame:
    """
    Cross-sectional momentum weights on a wide price panel (columns = symbols).
    At each rebalance date, rank by past lookback return and equal-weight top_k.
    Weights are held until next rebalance (forward filled), then shifted 1 day.
    """
    prices = price_panel.apply(pd.to_numeric, errors="coerce").sort_index()
    # formation return
    formation = prices / prices.shift(lookback) - 1.0
    # rebalance marks
    marks = formation.resample(rebalance).last().dropna(how="all")
    weights = pd.DataFrame(0.0, index=marks.index, columns=prices.columns)
    for dt, row in marks.iterrows():
        s = row.dropna().sort_values(ascending=False)
        picks = list(s.index[:top_k])
        if not picks:
            continue
        w = 1.0 / len(picks)
        for sym in picks:
            weights.loc[dt, sym] = w
    # align to daily calendar and shift for next-day holding
    daily_w = weights.reindex(prices.index).ffill().fillna(0.0)
    return daily_w.shift(1).fillna(0.0)


def panel_backtest(
    prices: pd.DataFrame,
    weights: pd.DataFrame,
    cost_bps: float = 10.0,
) -> pd.DataFrame:
    """Equal teaching portfolio backtest from daily weights (rows=date, cols=symbol)."""
    prices = prices.apply(pd.to_numeric, errors="coerce").sort_index()
    weights = weights.reindex(prices.index).fillna(0.0)
    rets = prices.pct_change().fillna(0.0)
    port_ret = (weights * rets).sum(axis=1)
    turn = weights.diff().abs().sum(axis=1).fillna(weights.abs().sum(axis=1))
    # approx: half-turn counted each side already in abs sum; use full sum * cost
    strat_ret = port_ret - turn * (cost_bps / 10000.0)
    # buy & hold equal weight of available names
    eq_w = prices.notna().astype(float)
    eq_w = eq_w.div(eq_w.sum(axis=1).replace(0, pd.NA), axis=0).fillna(0.0)
    bh = (eq_w * rets).sum(axis=1)
    return pd.DataFrame(
        {
            "strat_ret": strat_ret,
            "equity": (1.0 + strat_ret).cumprod(),
            "buy_hold": (1.0 + bh).cumprod(),
            "gross_exposure": weights.sum(axis=1),
            "turnover": turn,
        }
    )
