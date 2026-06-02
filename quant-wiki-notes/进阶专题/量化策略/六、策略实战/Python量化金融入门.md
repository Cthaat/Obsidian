---
title: Python量化金融入门
tags:
  - Python
  - 量化金融
  - 入门
created: 2026-06-02
type: note
source: python-quant-finance-intro.md
---

# Python量化金融入门

> [!note] 量化金融入门
> Python量化金融的基础入门，介绍量化金融的核心概念和Python实现。

## 量化金融核心概念

### 收益率
- 简单收益率：R = (P_t - P_{t-1}) / P_{t-1}
- 对数收益率：r = ln(P_t / P_{t-1})

### 风险
- 波动率：收益率的标准差
- VaR：在给定置信水平下的最大损失
- 最大回撤：净值从峰值到谷底的最大跌幅

### 风险调整收益
- 夏普比率：收益/波动率
- 索提诺比率：收益/下行波动率
- 卡玛比率：收益/最大回撤

## Python实现

```python
import numpy as np
import pandas as pd

# 计算关键指标
def calc_metrics(data):
    returns = data['close'].pct_change().dropna()
    
    metrics = {
        'annual_return': returns.mean() * 252,
        'annual_vol': returns.std() * np.sqrt(252),
        'sharpe': returns.mean() / returns.std() * np.sqrt(252),
        'max_drawdown': (data['close'] / data['close'].cummax() - 1).min()
    }
    
    return metrics
```

## 相关链接

- [[Python量化入门]]
- [[Python金融分析课程]]
- [[量化投资完全指南]]
- [[../目录|量化策略总览]]
