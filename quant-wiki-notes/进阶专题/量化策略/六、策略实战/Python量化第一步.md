---
title: Python量化第一步
date: 2026-06-02
tags:
  - Python
  - 量化入门
  - 第一步
created: 2026-06-02
type: note
source: python-quant-step1.md
aliases: []
updated: 2026-06-02
---

# Python量化第一步

> [!note] 本篇定位：环境搭建 + 第一个脚本
> 这是整个 Python 量化系列的**起点**——只做一件事：把环境装好，跑通"拉一只股票的日线 → 画出收盘价 → 算一段简单收益率"。不讲策略、不讲回测。数据处理的细节交给 [[Python量化入门]]，回测引擎交给 [[Python量化进阶]]。先让代码在你电脑上**真正跑起来**，比什么都重要。

## 一、为什么用 conda 而不是裸 pip

量化要装的库（pandas、numpy、matplotlib）底层依赖 C/Fortran 编译的数值计算组件，裸 `pip` 在 Windows 上常因缺编译器而失败。Anaconda/Miniconda 自带预编译的科学计算栈，并能用**虚拟环境**隔离项目，避免"装新库把旧项目搞崩"。

```mermaid
graph LR
    A[装 Miniconda] --> B[建独立环境 quant]
    B --> C[在环境内装库]
    C --> D[写脚本 / 开 Jupyter]
    D --> E[跑通第一个脚本]
```

> [!tip] Miniconda vs Anaconda
> Anaconda 体积大（数 GB，预装上百个库）；**Miniconda** 只含 conda 本体，按需安装，更干净。新手推荐 Miniconda。

## 二、安装 Python 环境

### 1. 下载并安装 Miniconda

```bash
# 下载地址：https://docs.conda.io/en/latest/miniconda.html
# 选对应操作系统（Windows / macOS / Linux）和 64 位版本
# Windows 安装时勾选 "Add to PATH"（或安装后手动配置）
```

安装完成后，验证：

```bash
conda --version      # 出现 conda 24.x.x 即成功
python --version     # Python 3.11.x（示例）
```

### 2. 创建独立的量化环境

```bash
# 新建名为 quant 的环境，指定 Python 版本
conda create -n quant python=3.11 -y

# 激活环境（每次开新终端都要先激活）
conda activate quant
# 激活后命令行前会出现 (quant) 前缀
```

> [!warning] 最常见的第一个坑：忘记激活环境
> 装库前没 `conda activate quant`，库会装到 base 环境；之后脚本"找不到模块"或"版本对不上"，多半是环境没激活。**认准命令行前缀 `(quant)`**。

## 三、安装量化常用库

```bash
# 在已激活的 quant 环境内执行
pip install pandas numpy matplotlib akshare
```

| 库 | 作用 | 本系列用途 |
|------|------|-----------|
| `akshare` | 免费财经数据接口 | 拉股票/指数行情 |
| `pandas` | 表格数据处理 | 存放与清洗行情（详见 [[Python量化入门]]） |
| `numpy` | 数值/向量化计算 | 收益、矩阵运算（详见 [[NumPy与Pandas量化指南]]） |
| `matplotlib` | 绘图 | 画价格曲线 |

> [!tip] 中文绘图乱码预防
> matplotlib 默认不显示中文，下面脚本里会统一设置字体，避免标题变成方框。

## 四、第一个脚本：拉数据 → 画图 → 算收益

下面这段是**完整可运行**的最小脚本。逐块读注释即可理解每一步在做什么。

```python
import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# --- 0. 让 matplotlib 正常显示中文与负号 ---
plt.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS"]  # Win用SimHei，Mac可用后者
plt.rcParams["axes.unicode_minus"] = False

# --- 1. 拉取一只股票的日线（以平安银行 000001 为例）---
df = ak.stock_zh_a_hist(
    symbol="000001",          # 股票代码（示例）
    period="daily",           # 日线
    start_date="20230101",
    end_date="20240101",
    adjust="qfq",             # 前复权：消除分红送股造成的价格跳空
)

print(df.shape)               # 看有多少行多少列（示例：(243, 11)）
print(df.columns.tolist())    # akshare 返回的是中文列名
```

> [!important] 第一步就要懂复权
> `adjust="qfq"`（前复权）很关键：未复权价格在除权日会"凭空跳水"，直接算收益会得到一个虚假的大跌。**算收益、画长期曲线一律用前复权。** 不复权（`adjust=""`）只适合看当日真实成交价。

继续处理数据并绘图：

```python
# --- 2. 把"日期"设为索引，并转成真正的时间类型 ---
df["日期"] = pd.to_datetime(df["日期"])
df = df.set_index("日期").sort_index()   # 排序保证时间从早到晚

# --- 3. 取出收盘价，画收盘价曲线 ---
close = df["收盘"]                        # 一个以日期为索引的 Series

plt.figure(figsize=(10, 4))
close.plot(title="000001 收盘价（示例）", grid=True)
plt.ylabel("价格（元）")
plt.tight_layout()
plt.savefig("close_price.png", dpi=120)   # 存成图片，避免无界面环境弹窗报错
plt.show()
```

```python
# --- 4. 计算简单收益率 ---
# 日收益率 r_t = P_t / P_{t-1} - 1，pct_change 一行搞定
df["日收益率"] = close.pct_change()

# 区间累计收益（净值 - 1）：把每日 (1+r) 连乘
total_return = (1 + df["日收益率"]).prod() - 1

# 也可以直接用首尾价格验证（应与上面接近）
simple_check = close.iloc[-1] / close.iloc[0] - 1

print(f"区间累计收益: {total_return:.2%}")   # 示例：12.34%
print(f"首尾价格验证: {simple_check:.2%}")   # 两者应基本一致
print(df`"收盘", "日收益率"`.tail())        # 看最后几行
```

> [!note] 运行结果该长什么样
> 你会得到一张收盘价折线图（`close_price.png`），以及一行形如"区间累计收益: 12.34%"的输出。看到这些，说明环境与数据链路已经**完全打通**——量化的地基就算打好了。

## 五、把脚本搬进 Jupyter（推荐）

交互式探索数据时，Jupyter 比直接跑 `.py` 更顺手（可分块运行、即时看图）。

```bash
# 在 quant 环境内安装并启动
pip install jupyterlab
jupyter lab            # 浏览器自动打开，新建 Notebook 逐块粘贴上面的代码
```

## 六、常见误区 / 踩坑

| 误区 | 现象 | 正确做法 |
|------|------|----------|
| 忘记 `conda activate quant` | 报 `ModuleNotFoundError` | 认准 `(quant)` 前缀再装/再跑 |
| 用未复权价算长期收益 | 除权日"假暴跌"，收益失真 | `adjust="qfq"` 前复权 |
| 不把日期转 `datetime` | 排序/切片按字符串错乱 | `pd.to_datetime` + `set_index` |
| 数据没 `sort_index` | 时间倒序，`pct_change` 算反 | 取数后立即 `sort_index()` |
| 列名记成英文 | `KeyError: 'close'` | akshare 是中文列名"收盘" |
| 无界面环境直接 `plt.show()` | 报后端错误或卡住 | 先 `savefig` 存图 |
| 全部代码堆一行调试 | 出错难定位 | 分块运行（Jupyter）逐步验证 |

> [!warning] 不要在"第一步"就追求复杂
> 很多人一上来就想写带止损、带仓位管理的完整策略，结果卡在环境与数据格式上。**第一步的唯一目标是跑通数据链路。** 数据操作进阶看 [[Python量化入门]]，把信号变成净值看 [[Python量化进阶]]，想要端到端速览看 [[Python量化3小时精通]]。

## 相关链接

- [[Python量化入门]]
- [[Python量化3小时精通]]
- [[Python金融分析课程]]
- [[目录|量化策略总览]]
- [[Python量化进阶]]
- [[Python量化教程Runoo]]
- [[NumPy与Pandas量化指南]]

## 课程化学习补充

> [!important] 学习定位
> 量化策略是投资假设、数据工程、回测验证、风险预算和执行系统的组合，不是单一公式。本文仅用于学习、研究与复盘，不构成任何投资建议。

### 必须掌握的问题

- 假设是否可证伪
- 数据是否 point-in-time
- 绩效是否扣除真实成本
- 上线后是否监控衰减

### 实战应用流程

1. 先写清楚你的投资假设：为什么这个信号、资产或方法应该产生收益。
2. 明确数据口径：样本范围、更新时间、复权/分红/停牌处理和交易日历。
3. 做最小可行验证：先用简单规则验证方向，再逐步加入复杂模型。
4. 把成本和约束前置：手续费、滑点、冲击成本、保证金、流动性和容量都要进入测算。
5. 上线后持续复盘：记录信号、下单、成交、持仓、回撤和失效原因。

### 风险与失效条件

- 数据挖掘偏差
- 因子拥挤
- 换手过高
- 实盘偏离回测

### 复盘问题

- 这笔交易或这套模型赚的是什么钱：风险补偿、行为偏差、流动性溢价，还是偶然噪音？
- 如果市场环境反过来，最大亏损和最长恢复期会是多少？
- 当前结论是否依赖某个不可持续假设，例如低利率、低波动、充裕流动性或监管套利？
- 有没有一个更简单的基准策略能取得接近效果？

### 延伸学习

- [[量化投资完全指南]]
- [[回测质量门清单]]
- [[市场微观结构与交易执行]]
- [[量化风险管理体系]]

## 跨领域进阶扩展

> [!tip] 交易者视角
> 学到 `Python量化第一步` 时，不要只把它当成孤立知识点。把策略视为假设、数据、验证、组合和执行的整体工程。优秀投资交易者会把它放入“宏观背景 - 资产选择 - 估值/信号 - 组合风险 - 交易执行 - 复盘反馈”的闭环。

### 与其他知识的连接

- 收益来源和经济解释
- 数据清洗和偏差控制
- 回测、组合和风控
- 实盘衰减与策略迭代

### 进阶训练

1. 把策略假设写成可证伪命题
2. 建立基准策略比较
3. 把换手、容量和成本纳入绩效评价

### 能力验收

- 能否说清楚这个主题影响的是收益来源、风险来源、交易成本、流动性还是心理纪律？
- 能否指出它在什么市场环境、资产类别或交易周期中更有效？
- 能否把它写成一条可复盘的研究或交易规则？
- 能否说明如果判断错误，组合最大损失和退出机制是什么？

### 全局关联

- [[综合金融知识体系/金融投资全知识地图|金融投资全知识地图]]
- [[综合金融知识体系/优秀投资交易者能力地图|优秀投资交易者能力地图]]
- [[综合金融知识体系/一次性学习路线与复盘模板|一次性学习路线与复盘模板]]
