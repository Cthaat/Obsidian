---
title: Python量化环境搭建
date: 2026-07-13
tags:
  - 投资
  - 量化
  - 实操
  - Python
---

# Python量化环境搭建

> [!note] 核心问题
> 量化研究的第一步不是选策略，而是有一个**可复现、可隔离、可升级**的 Python 环境。本篇带你从零装到「能取数、能算、能画图、能回测」，并建立工程卫生习惯。

## 学习目标

读完这篇，你要能做到：

1. 用 venv 或 conda 创建独立环境，不污染系统 Python。
2. 安装量化最小依赖集并验证 import。
3. 规划项目目录，用 `requirements.txt` 锁定版本。
4. 知道 Jupyter 与脚本两种工作流如何分工。
5. 处理 Windows 上常见安装坑（路径、权限、镜像）。

## 你需要什么机器

| 项目 | 最低建议 | 说明 |
|---|---|---|
| 系统 | Windows 10/11、macOS、Linux | 本库用户多为 Windows |
| 内存 | 16GB 更舒服 | 8GB 可学日频，大数据吃力 |
| 磁盘 | 20GB+ 空余 | 数据与环境会涨 |
| Python | 3.10–3.12（64 位） | 与多数金融库兼容较好 |

## 路线选择：venv 还是 conda

| 方式 | 优点 | 缺点 | 适合 |
|---|---|---|---|
| **venv + pip** | 轻、标准、好理解 | 科学计算二进制有时折腾 | 多数学习者 |
| **Miniconda/Anaconda** | 解依赖强，文档多 | 体积大，环境易臃肿 | 怕编译问题的新手 |
| **Docker** | 最强复现 | 学习曲线 | 以后部署用 |

**本篇默认**：Miniconda 或 venv 二选一；命令以通用 pip 为主。

## 步骤一：安装 Python 发行版

### 选项 A：官方 Python + venv（轻）

1. 打开 [python.org](https://www.python.org/downloads/) 下载 64 位安装包。  
2. Windows 勾选 **Add python.exe to PATH**。  
3. 终端验证：

```powershell
python --version
pip --version
```

### 选项 B：Miniconda（省心）

1. 打开 [Miniconda](https://docs.conda.io/en/latest/miniconda.html) 安装。  
2. 打开 Anaconda Prompt 或已初始化的 PowerShell：

```powershell
conda --version
```

## 步骤二：创建隔离环境

### venv

```powershell
cd C:\Code
mkdir quant-lab
cd quant-lab
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

若 PowerShell 禁止脚本，可临时：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### conda

```powershell
conda create -n quant-lab python=3.11 -y
conda activate quant-lab
python -m pip install --upgrade pip
```

> [!tip]
> 环境名、项目文件夹不要叫 `akshare`、`numpy` 等包名，避免导入阴影。

## 步骤三：安装最小依赖集

### 研究最小集

```powershell
pip install numpy pandas matplotlib jupyter notebook
```

### 数据（A 股常用）

```powershell
pip install akshare
# 可选
pip install tushare baostock yfinance
```

国内网络可加清华镜像：

```powershell
pip install akshare -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 回测（先装一个）

```powershell
pip install backtrader
# 或更轻量
pip install backtesting
```

### 验证脚本 `check_env.py`

```python
import sys
print("Python", sys.version)

import numpy as np
import pandas as pd
import matplotlib
print("numpy", np.__version__)
print("pandas", pd.__version__)
print("matplotlib", matplotlib.__version__)

try:
    import akshare as ak
    print("akshare", getattr(ak, "__version__", "ok"))
except Exception as e:
    print("akshare import failed:", e)

print("ENV OK")
```

运行：

```powershell
python check_env.py
```

## 步骤四：推荐项目结构

```text
quant-lab/
  .venv/                 # 或 conda 环境不在此
  data/
    raw/                 # 原始拉取，尽量不改
    processed/           # 清洗后
  notebooks/             # 探索性分析
  src/
    data_loader.py
    features.py
    backtest_runner.py
  strategies/
    dual_ma.py
  reports/               # 图表与回测输出
  requirements.txt
  README.md
  check_env.py
```

原则：

- **原始数据不可变**；清洗写新文件。  
- 策略参数写在配置或函数参数，不散落魔法数。  
- Notebook 负责探索，稳定逻辑迁到 `src/`。

## 步骤五：锁定依赖

```powershell
pip freeze > requirements.txt
```

新机器复现：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

研究笔记里记录：

| 字段 | 例 |
|---|---|
| 日期 | 2026-07-13 |
| Python | 3.11.x |
| 关键库版本 | akshare / pandas / backtrader |
| 数据区间 | 2020-01-01 ~ 2023-12-31 |
| 复权 | qfq |

## Jupyter 工作流

```powershell
pip install jupyter
jupyter notebook
# 或
pip install jupyterlab
jupyter lab
```

建议：

| 用途 | 用 Notebook | 用 .py 脚本 |
|---|---|---|
| 探索接口、画图 | 是 | 否 |
| 定时拉数、正式回测 | 否 | 是 |
| 分享教学 | 是 | 可 |
| Git 协作 | 注意输出清理 | 更干净 |

## IDE 建议

| 工具 | 适合 |
|---|---|
| VS Code + Python 扩展 | 通用，本环境常见 |
| PyCharm | 工程大时 |
| 聚宽/QuantConnect 网页 IDE | 零安装研究 |
| Windows Terminal | 多环境切换 |

在 VS Code 中选择解释器为 `.venv\Scripts\python.exe`。

## Windows 常见坑

| 现象 | 可能原因 | 处理 |
|---|---|---|
| `python` 不是命令 | 未进 PATH | 重装勾选 PATH 或用完整路径 |
| pip 装到别的 Python | 多版本混乱 | `python -m pip` |
| SSL / 超时 | 网络 | 换镜像源 |
| 编译失败 | 缺 wheel | 换版本或 conda |
| 杀毒拦截 | 误报 | 加白名单到项目目录 |
| 中文路径问题 | 部分旧库 | 项目放 `C:\Code\...` |

## 与「实盘环境」的边界

本篇是**研究环境**。实盘还需要：

- 研究 / 仿真 / 生产隔离；  
- 密钥不进 Git；  
- 日志与一键停止；  
- 合规与权限。  

工程清单见本库 [[Python量化环境配置]] 与 [[量化部署/目录]]。阶段零先把研究环境做稳。

## 可选：下一步加装

| 目标 | 包 |
|---|---|
| 统计与检验 | scipy statsmodels |
| 加速 | polars numba |
| 可视化增强 | plotly mplfinance |
| 机器学习 | scikit-learn（先别上深度学习） |
| 本地交易框架 | vnpy（单独环境，避免依赖地狱） |

vn.py 建议**单独 conda 环境**，不要和轻量研究环境搅在一起。

## 30 分钟验收清单

- [ ] 独立环境可 activate  
- [ ] `check_env.py` 打印 ENV OK  
- [ ] 能 `import akshare` 或 `yfinance`  
- [ ] 项目目录结构已建  
- [ ] `requirements.txt` 已生成  
- [ ] README 写了如何复现  

## 常见误区

| 误区 | 更好的理解 |
|---|---|
| 用系统 Python 全局乱装 | 隔离环境是基本功 |
| 一上来装完整数据科学全家桶 | 最小集能跑再扩展 |
| 不记录版本 | 三个月后无法复现实验 |
| Notebook 里堆 2000 行策略 | 稳定逻辑模块化 |
| 环境坏了就重装系统 | 删环境重建即可 |

## 练习：环境体检表

| 检查项 | 你的结果 |
|---|---|
| Python 版本 |  |
| 环境路径 |  |
| pandas 版本 |  |
| 数据库 |  |
| 回测库 |  |
| 项目根目录 |  |
| requirements 是否入库 |  |

## 官网与依赖核对（补充）

| 项 | 建议 |
|---|---|
| Python | 3.10–3.12 常用；AKShare 文档要求 ≥3.9，常推荐 3.11.x |
| 数据库 | `pip install akshare --upgrade`（见 [安装页](https://akshare.akfamily.xyz/installation.html)） |
| 回测 | `pip install backtrader` 或平台研究环境 |
| 工程自检 | quant-lab：`python scripts/run_stage0_check.py --with-synthetic-backtest` |
| 总表 | [[全库网络资源总表]] |

国内 pip 镜像示例（可选）：`-i https://pypi.tuna.tsinghua.edu.cn/simple`

## 相关概念

[[从零开始的第一条实操路线]] [[数据源全景与选型]] [[回测框架选型与最小示例]] [[Python量化环境配置]] [[AKShare安装配置]] [[全库网络资源总表]] [[全库使用验收看板]]
