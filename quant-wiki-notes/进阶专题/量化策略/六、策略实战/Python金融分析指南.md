---
title: Python金融分析指南
tags:
  - Python
  - 金融分析
  - 指南
created: 2026-06-02
type: note
source: python-financial-analysis-guide.md
---

# Python金融分析指南

> [!note] 金融分析指南
> Python金融分析实战指南，介绍常用金融分析方法和Python实现。

## 常用分析方法

### 1. 技术分析
- 移动平均线
- RSI指标
- MACD指标
- 布林带

### 2. 基本面分析
- 财务指标分析
- 估值分析
- 行业对比

### 3. 风险分析
- VaR计算
- 最大回撤
- 波动率分析

## 代码示例

```python
# RSI计算
def calc_rsi(data, period=14):
    delta = data['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
```

## 相关链接

- [[Python金融分析课程]]
- [[Python量化入门]]
- [[Python量化金融入门]]
- [[../目录|量化策略总览]]
