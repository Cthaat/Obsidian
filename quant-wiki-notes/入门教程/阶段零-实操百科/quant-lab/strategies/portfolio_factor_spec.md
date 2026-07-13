# portfolio_v0.1 / factor_score_v0.1（教学）

## 组合层 equal / inv_vol

| 字段 | 内容 |
|---|---|
| 池 | `data/watchlists/demo_pool.txt` |
| equal | 再平衡日对可交易名等权 |
| inv_vol | 权重 ∝ 1/波动（简化风险平价思想） |
| 再平衡 | 默认 `ME`（月尾，以 pandas 为准） |
| 成本 | cost_bps |
| 可选 | max_weight 单票上限 |

```text
python scripts/pull_watchlist.py
python scripts/run_equal_weight_rebalance.py --scheme equal --rebalance ME
python scripts/run_equal_weight_rebalance.py --scheme inv_vol --max-weight 0.4
```

## 因子打分 factor_score_v0.1（仅价量）

| 因子 | 定义 |
|---|---|
| momentum | lookback 收益，截面 z-score |
| low_vol | -滚动波动，截面 z-score |
| 合成 | 等权平均 z 后取 top_k 等权 |

**明确不做**：基本面 PIT 因子（避免教学脚本假装有公告日对齐）。

```text
python scripts/run_factor_score.py --top-k 2 --mom-lookback 20 --vol-lookback 20
```
