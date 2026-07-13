from __future__ import annotations

"""Optional Backtrader dual-MA strategy. Requires: pip install backtrader"""


def build_dual_ma_strategy(fast: int = 5, slow: int = 20):
    import backtrader as bt

    class DualMAStrategy(bt.Strategy):
        params = dict(fast=fast, slow=slow)

        def __init__(self):
            self.fast_ma = bt.ind.SMA(period=self.p.fast)
            self.slow_ma = bt.ind.SMA(period=self.p.slow)
            self.crossover = bt.ind.CrossOver(self.fast_ma, self.slow_ma)

        def next(self):
            if not self.position and self.crossover[0] > 0:
                self.buy()
            elif self.position and self.crossover[0] < 0:
                self.close()

    return DualMAStrategy
