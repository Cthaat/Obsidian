# ts_momentum_v0.1 + cross_section_v0.1（教学）

> 非投资建议。规则约束见 [[A股交易规则实操要点]]、[[动量策略实操]]。

## 时序动量 ts_momentum_v0.1

| 字段 | 内容 |
|---|---|
| 逻辑 | 过去 lookback 日收益 > 0 则下一期做多，否则空仓 |
| 默认 | lookback=20, skip=0, cost_bps=10 |
| 可选风控 | `--max-dd 0.2` 权益回撤熔断（简化） |
| 未建模 | 涨跌停、印花税分边、精确 T+1 |

```text
python scripts/pull_akshare_example.py --symbol 000001
python scripts/run_ts_momentum.py --symbol 000001 --lookback 20
python scripts/run_ts_momentum.py --symbol 000001 --lookback 60 --max-dd 0.25
```

## 截面动量 xs_mom_v0.1

| 字段 | 内容 |
|---|---|
| 股票池 | `data/watchlists/demo_pool.txt`（请换成你的池） |
| 逻辑 | 每周按 lookback 收益排序，等权持有 top_k |
| 默认 | lookback=20, top_k=2, rebalance=W, cost_bps=15 |
| 警告 | 池子极小，只为学流程；有幸存者/流动性未处理 |

```text
python scripts/pull_watchlist.py
python scripts/run_cross_section_momentum.py --top-k 2 --lookback 20
```
