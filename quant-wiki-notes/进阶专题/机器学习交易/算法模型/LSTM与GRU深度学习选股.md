---
topic: 机器学习交易
parent: 机器学习交易
tags: [LSTM, GRU, deep-learning, 选股]
created: 2026-06-02
---

# LSTM与GRU深度学习选股

> [!note] 概述
> 利用LSTM和GRU等序列深度学习模型进行A股量化选股。通过捕捉量价数据的时序特征，构建优于传统线性因子的选股信号。

## LSTM模型原理

LSTM通过三个门控结构解决传统RNN的梯度消失问题：

```
遗忘门(f_t): 决定丢弃哪些旧信息
输入门(i_t): 决定存储哪些新信息
输出门(o_t): 决定输出什么
细胞状态(C_t): 长期记忆通道
```

```
公式：
f_t = σ(W_f · [h_{t-1}, x_t] + b_f)
i_t = σ(W_i · [h_{t-1}, x_t] + b_i)
C̃_t = tanh(W_C · [h_{t-1}, x_t] + b_C)
C_t = f_t * C_{t-1} + i_t * C̃_t
o_t = σ(W_o · [h_{t-1}, x_t] + b_o)
h_t = o_t * tanh(C_t)
```

## GRU简化版

GRU将遗忘门和输入门合并为"更新门"，减少参数量：

- 更新门 z_t：控制保留多少历史信息
- 重置门 r_t：控制遗忘多少历史信息
- 比LSTM少约25%参数

## A股选股实战架构

### 特征设计

常用量价特征（18个标准特征）：

| 类别 | 特征 |
|------|------|
| 价格 | open, high, low, close, vwap |
| 成交量 | volume, amount |
| 收益率 | 1d/5d/10d/20d return |
| 波动率 | 5d/10d/20d volatility |
| 技术指标 | RSI, MACD, KDJ, BIAS |

### 数据窗口
```
时间窗口 = 40天（输入40个交易日序列）
特征维度 = 18个量价特征
输入shape = (batch, 40, 18)

标签 = 未来5天收益率（回归）/ 涨跌分类
```

### 模型结构

```python
import torch
import torch.nn as nn

class LSTMStockSelector(nn.Module):
    def __init__(self, input_dim=18, hidden_dim=64,
                 num_layers=2, dropout=0.2):
        super().__init__()
        self.lstm = nn.LSTM(
            input_dim, hidden_dim, num_layers,
            batch_first=True, dropout=dropout
        )
        self.fc = nn.Sequential(
            nn.Linear(hidden_dim, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, 1)  # 预测收益率
        )

    def forward(self, x):
        # x: (batch, 40, 18)
        out, (h_n, c_n) = self.lstm(x)
        # 取最后时刻的输出
        last_out = out[:, -1, :]  # (batch, hidden_dim)
        return self.fc(last_out)
```

## 回测效果参考

基于西南证券研报的实测数据：

| 模型 | RankIC | 多头年化 | 最大回撤 | 多空年化 |
|------|--------|---------|---------|---------|
| GRU | 3.14% | 11.40% | 42.78% | - |
| AE_GRU | 1.29% | 4.82% | - | 8.78% |
| **GAN_GRU** | **7.03%** | **18.00%** | 41.75% | **46.64%** |

> GAN_GRU在沪深300指数增强中相对指数年化超额收益率15.02%

## 实战部署架构

### Python + MT5 两组件架构

```
┌──────────────────────────────────────┐
│  Python LSTM 机器人                    │
│  · 市场分析、模式识别、信号生成        │
│  · 定期训练LSTM模型                   │
│  · 生成买卖信号                       │
└──────────────┬───────────────────────┘
               │ WebSocket/API
┌──────────────▼───────────────────────┐
│  MT5 执行引擎                         │
│  · 订单执行                           │
│  · 仓位管理                           │
│  · 风控监控                           │
└──────────────────────────────────────┘
```

### 训练流程

1. 每周/每月用最新数据重新训练模型
2. 用Walk-Forward验证避免过拟合
3. 在模拟盘中运行至少3个月后切换实盘
4. 监控训练集与实盘表现的差距

## 注意事项

- **过拟合是第一大敌**：金融数据信噪比极低，模型容易记忆噪声
- **分布漂移**：过去训练的模型可能不适应新的市场环境
- **标签泄漏**：确保标签只使用未来信息（而非当前）
- **成本考量**：高频交易的交易成本可能吞噬所有Alpha
- **样本量需求**：LSTM需要较大样本，小样本慎用
