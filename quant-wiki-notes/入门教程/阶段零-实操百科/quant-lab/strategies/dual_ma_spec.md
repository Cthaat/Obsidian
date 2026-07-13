# dual_ma_v0.1 策略说明书（教学）

> 与 [[第一个可回测策略]]、[[A股交易规则实操要点]] 对齐。数字为假设，不构成投资建议。

| 字段 | 内容 |
|---|---|
| 名称 | dual_ma_v0.1 |
| 市场 | A 股单标的（默认 000001） |
| 频率 | 日频 |
| 逻辑 | 短期均线上穿/下穿长期均线，趋势跟随 |
| 默认参数 | fast=5, slow=20 |
| 信号时点 | 收盘确认，向量化实现用 `shift(1)` 下一期持仓 |
| 方向 | 只做多 |
| 成本假设 | 向量化：单边换仓 cost_bps=10（近似）；Backtrader：commission=0.0003 示意 |
| 未建模 | 印花税分边、涨跌停、停牌、精确 T+1 路径、最小佣金 5 元 |
| 数据 | `data/processed/{symbol}_ohlcv.csv`，复权见 `.meta.json` |
| 基准 | 同学段买入持有（脚本内 `buy_hold`） |
| 失效条件 | 震荡市高频假信号；成本升高后收益转负；单年行情依赖 |

## 运行

```text
python scripts/pull_akshare_example.py --symbol 000001
python scripts/run_dual_ma.py --symbol 000001
python scripts/run_backtrader_dual_ma.py --symbol 000001
```

## 实验笔记

每改参数升版本（v0.2...），并写 EXP 笔记：见 [[研究笔记与实验工作流]]。
