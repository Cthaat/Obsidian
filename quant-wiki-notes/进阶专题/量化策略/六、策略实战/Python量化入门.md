---
title: Python量化入门
tags:
  - Python
  - 量化入门
  - 编程
created: 2026-06-02
type: note
source: python-quant-beginner-to-advanced.md, python-quant-step1.md
---

# Python量化入门

> [!note] Python量化入门
> Python是量化投资最主流的编程语言，掌握Python是量化入门的第一步。

## 为什么选择Python

- **生态丰富**：pandas、numpy、scipy等库
- **易于学习**：语法简洁，上手快
- **社区活跃**：大量量化开源项目
- **通用性强**：数据分析、机器学习、Web开发

## 核心库

| 库 | 用途 | 说明 |
|---|------|------|
| pandas | 数据处理 | DataFrame操作 |
| numpy | 数值计算 | 矩阵运算 |
| matplotlib | 数据可视化 | 图表绘制 |
| scipy | 科学计算 | 统计分析 |
| statsmodels | 统计建模 | 回归分析 |
| scikit-learn | 机器学习 | 模型训练 |

## 学习路径

1. **Python基础**：变量、循环、函数
2. **数据处理**：pandas操作
3. **可视化**：matplotlib绑图
4. **统计分析**：描述统计、假设检验
5. **策略开发**：信号生成、回测
6. **实盘应用**：API接口、自动化

## 第一个量化策略

```python
import pandas as pd
import matplotlib.pyplot as plt

# 双均线策略
data = pd.read_csv('stock_data.csv')
data['SMA5'] = data['close'].rolling(5).mean()
data['SMA20'] = data['close'].rolling(20).mean()

# 信号
data['signal'] = 0
data.loc[data['SMA5'] > data['SMA20'], 'signal'] = 1
data.loc[data['SMA5'] < data['SMA20'], 'signal'] = -1

# 绘图
data[['close', 'SMA5', 'SMA20']].plot()
plt.show()
```

## 相关链接

- [[Python量化进阶]]
- [[Python量化3小时精通]]
- [[量化工具链NumPy与Pandas]]
- [[../目录|量化策略总览]]
