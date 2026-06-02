---
title: Python量化第一步
tags:
  - Python
  - 量化入门
  - 第一步
created: 2026-06-02
type: note
source: python-quant-step1.md
---

# Python量化第一步

> [!note] 量化学习第一步
> 量化学习的第一步，从环境搭建到编写第一个量化策略。

## 环境搭建

### 安装Python
```bash
# 推荐使用Anaconda
# 下载地址：https://www.anaconda.com/download
```

### 安装量化库
```bash
pip install pandas numpy matplotlib tushare akshare
```

## 第一个量化策略

```python
import pandas as pd
import akshare as ak

# 获取股票数据
stock = ak.stock_zh_a_hist(symbol="000001", period="daily", 
                           start_date="20230101", end_date="20240101")

# 计算均线
stock['MA5'] = stock['收盘'].rolling(5).mean()
stock['MA20'] = stock['收盘'].rolling(20).mean()

# 生成信号
stock['signal'] = 0
stock.loc[stock['MA5'] > stock['MA20'], 'signal'] = 1

# 计算收益
stock['returns'] = stock['收盘'].pct_change()
stock['strategy'] = stock['signal'].shift(1) * stock['returns']

print(f"策略总收益: {(1 + stock['strategy']).prod() - 1:.2%}")
```

## 相关链接

- [[Python量化入门]]
- [[Python量化3小时精通]]
- [[Python金融分析课程]]
- [[../目录|量化策略总览]]
