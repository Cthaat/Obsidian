---
title: "代码开源！如何使用DeepSeek-R1或ChatGPT与Langchain构建专业金融分析师"
category: "AI+量化"
tags: [AI+量化, 量化, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

![](https://fastly.jsdelivr.net/gh/bucketio/img11@main/2024/10/21/1729466068183-23134fce-3131-4262-b18c-f378d71af4f6.gif)

# 代码开源！如何使用DeepSeek-R1或ChatGPT与Langchain构建专业金融分析师

在快速变化的金融市场中，**如何用人工智能来助力投资决策**正成为越来越多投资人的关注重点。利用大模型进行**股票

> [!note] 股票
> 公司所有权的凭证，代表股东对公司资产和收益的权益
分析**和**新闻洞察**，不仅能让我们高效获取关键数据，还能生成更具参考价值的投资建议。本文将带你一步步搭建两个实用场景：

1. **第一部分**：通过 **DeepSeek-R1** 打造 **股票分析代理**，包括获取股价、计算技术指标、评估财务指标，并输出可执行的结论。  
2. **第二部分**：通过 **ChatGPT** 聚焦 **新闻内容分析**，提取实时新闻并进行情感分析，为投资决策提供更全面的参考。

> 如果你是金融从业者、量化工程师或数据科学家，这篇文章将为你提供几乎完整的示例代码，帮助你快速搭建自己的智能分析Agent。

## 第一部分：使用DeepSeek-R1构建股票分析代理

在这一部分，我们将通过 **DeepSeek-R1** 模型完成**股价与财务数据**的分析。主要包括以下步骤：

1. 环境准备与安装
2. 获取股票历史价格及关键技术指标（RSI、MACD、VWAP等）
3. 获取财务指标（如市盈率、市净率、债务股本比、利润率等）
4. 通过 **LangChain** 与 **LangGraph** 进行流程化编排，并使用 **DeepSeek-R1** 提供分析生成

### 1. 环境安装

请先安装所需库（请注意，DeepSeek-R1 依赖 [Ollama](https://ollama.人工智能/) 或相应本地部署环境）：

```bash
pip install -U langgraph langchain langchain-ollama pandas ta python-dotenv yfinance
```

并在项目目录下创建一个 `.env` 文件，用于存放你的自定义环境变量（若有）：

```
# 可选
DEEPSEEK_API_KEY=your_deepseek_api_key
```

如果不需要私有API，可忽略。

### 2. 获取股票与技术指标

在开始前，确保你已经安装了 `yfinance` 用来获取股票数据，`ta` 用来计算常见技术指标。下面的示例工具函数会获取指定股票的**最近24周**的价格数据，并计算**RSI**、**MACD**、**Stochastic Oscillator** 与 **VWAP** 等常用技术指标。

```python
from typing import Union, Dict, TypedDict
import pandas as pd
import yfinance as yf
import datetime as dt

# TA 库
from ta.momentum import RSIIndicator, StochasticOscillator
from ta.trend import MACD
from ta.volume import volume_weighted_average_price

def get_stock_prices(ticker: str) -> Union[Dict, str]:
    """获取指定股票的历史价格数据和关键技术指标。"""
    try:
        data = yf.download(
            ticker,
            start=dt.datetime.now() - dt.timedelta(weeks=24*3),
            end=dt.datetime.now(),
            interval='1wk'
        )
        df = data.copy()
        data.reset_index(inplace=True)
        data.Date = data.Date.astype(str)
        
        indicators = {}
        
        rsi_series = RSIIndicator(df['Close'], window=14).rsi().iloc[-12:]
        indicators["RSI"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in rsi_series.dropna().to_dict().items()
        }
        
        sto_series = StochasticOscillator(
            df['High'], df['Low'], df['Close'], window=14
        ).stoch().iloc[-12:]
        indicators["Stochastic_Oscillator"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in sto_series.dropna().to_dict().items()
        }
        
        macd = MACD(df['Close'])
        macd_series = macd.macd().iloc[-12:]
        indicators["MACD"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in macd_series.to_dict().items()
        }
        
        macd_signal_series = macd.macd_signal().iloc[-12:]
        indicators["MACD_Signal"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in macd_signal_series.to_dict().items()
        }
        
        vwap_series = volume_weighted_average_price(
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            volume=df['Volume'],
        ).iloc[-12:]
        indicators["vwap"] = {
            date.strftime('%Y-%m-%d'): float(value) 
            for date, value in vwap_series.to_dict().items()
        }
        
        return {
            'stock_price': data.to_dict(orient='records'),
            'indicators': indicators
        }

    except Exception as e:
        return f"Error fetching price data: {str(e)}"
```

### 3. 获取财务指标

财务健康指标包括 **P/E、Price-to-Book、Debt-to-Equity、Profit Margins** 等：

```python
def get_financial_metrics(ticker: str) -> Union[Dict, str]:
    """获取指定股票的关键财务比率。"""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'pe_ratio': info.get('forwardPE'),
            'price_to_book': info.get('priceToBook'),
            'debt_to_equity': info.get('debtToEquity'),
            'profit_margins': info.get('profitMargins')
        }
    except Exception as e:
        return f"Error fetching ratios: {str(e)}"
```

### 4. 使用LangGraph + DeepSeek-R1进行综合分析

#### 4.1 环境配置

我们使用 **LangGraph** 来串联对话流与工具调用。此时的大模型将选用 **DeepSeek-R1**，需要配合 [OllamaLLM](https://pypi.org/project/langchain-ollama/) 来调用本地或服务器端的大模型。

```python
import dotenv
dotenv.load_dotenv()

from langgraph.graph import StateGraph, START, END
from langchain_core.nodes import ToolNode
from typing import TypedDict

class State(TypedDict):
    messages: list
    stock: str

graph_builder = StateGraph(State)
```

#### 4.2 绑定DeepSeek-R1模型

```python
from langchain_ollama.llms import OllamaLLM

# 初始化 Ollama + DeepSeek-R1
llm = OllamaLLM(model="deepseek-r1:1.5b")
```

#### 4.3 构建Prompt并绑定工具

我们希望代理能：  
1. 获取股票历史与技术指标  
2. 获取财务指标  
3. 综合分析并输出可阅读的结论

```python
from langchain.schema import SystemMessage
from langchain_core.tools import tool

FUNDAMENTAL_ANALYST_PROMPT = """
You are a fundamental analyst specializing in evaluating company performance based on stock prices, technical indicators, and financial metrics.
Your task: Provide a comprehensive summary for {company}.

Steps to follow:
1. Use get_stock_prices and get_financial_metrics to gather data.
2. Analyze trends, potential support/resistance, and financial health.
3. Provide a concise, objective summary in JSON with:
   - "stock": <symbol>
   - "price_analysis": ...
   - "technical_analysis": ...
   - "financial_analysis": ...
   - "final_summary": ...
   - "recommendation": ...
"""

def fundamental_analyst(state: State):
    system_message = SystemMessage(
        content=FUNDAMENTAL_ANALYST_PROMPT.format(company=state['stock'])
    )
    messages = [system_message] + state["messages"]
    # 直接调用 llm.invoke
    result = llm.invoke(messages)
    return {"messages": result}
```

#### 4.4 将工具节点与分析节点接入工作流

```python
tools = [get_stock_prices, get_financial_metrics]

# 将工具封装为 LangGraph 节点
graph_builder.add_node('fundamental_analyst', fundamental_analyst)
graph_builder.add_edge(START, 'fundamental_analyst')

def tools_condition(state: State) -> bool:
    return True

graph_builder.add_node(ToolNode(tools))
graph_builder.add_conditional_edges('fundamental_analyst', tools_condition)
graph_builder.add_edge('tools', 'fundamental_analyst')

graph = graph_builder.compile()
```

#### 4.5 执行示例

```python
events = graph.stream({
    "messages": [("user", "Should I buy this stock?")],
    "stock": "AAPL"
}, stream_mode='values')

for event in events:
    if 'messages' in event:
        print(event['messages'][-1].content)
```

输出可能类似：

```json
{
  "stock": "AAPL",
  "price_analysis": "Recent price shows an upward trend with moderate volatility...",
  "technical_analysis": "RSI is around 62 indicating slightly overbought range...",
  "financial_analysis": "PE ratio is 28.5, which is higher than industry median...",
  "final_summary": "Apple maintains strong fundamentals but currently trades at a premium...",
  "recommendation": "Consider a partial buy if you anticipate continued revenue growth."
}
```

---

## 第二部分：使用ChatGPT构建新闻分析代理

在完成股票与财务数据分析后，还需要关注**市场情绪**与**实时新闻动态**。本部分将介绍如何使用 **ChatGPT**（或OpenAI GPT-4）来分析相关新闻，给出情感判断与投资建议。

### 1. 主要功能

- **抓取与股票相关的新闻**（使用Yahoo Finance）
- **提取网页全文**（使用MarkItDown等工具）
- **对新闻进行情感分析**（Positive, Negative, Neutral）
- **基于综合新闻观点给出投资建议**

### 2. 安装与环境准备

若已安装 `langgraph`、`langchain` 等，可跳过此步骤，仅需要确认**OpenAI**依赖已安装：

```bash
pip install openai
```

并在 `.env` 文件中增加：

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 获取相关新闻链接

```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    获取与指定股票相关的新闻列表。
    """
    try:
        ticker = yf.Ticker(stock)
        news = ticker.news

        if not news:
            print(f"No news found for {stock}.")
            return []
        
        relevant_news = [
            item for item in news if item.get('content', {}).get('contentType') == 'STORY'
        ]

        all_news = []
        for i, item in enumerate(relevant_news):
            try:
                content = item.get('content', {})
                current_news = {
                    'title': content.get('title'),
                    'summary': content.get('summary'),
                    'url': content.get('canonicalUrl', {}).get('url'),
                    'pubdate': content.get('pubDate', '').split('T')[0],
                }
                all_news.append(current_news)
            except Exception as e:
                print(f"Error processing news {i}: {e}")
                continue

        return all_news
    except Exception as e:
        print(f"An error occurred while fetching news for {stock}: {e}")
        return []
```

### 4. 提取并清洗新闻正文

```python
from markitdown import MarkItDown
import requests
import re

session = requests.Session()
session.headers.update({
    'User-Agent': 'python-requests/2.32.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
})
md = MarkItDown(requests_session=session)

def remove_links(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'[#*()+\-\n]', '', text)
    text = re.sub(r'/\S*', '', text)
    text = re.sub(r'  ', '', text)
    return text

def extract_news(link):
    extracted = md.convert(link)
    title = extracted.title.strip()
    content = extracted.text_content.strip()
    return title + "\n" + remove_links(content)
```

### 5. 获取完整新闻内容

```python
def extract_full_news(stock: str) -> list:
    news_list = get_news(stock)
    for i, item in enumerate(news_list):
        try:
            full_text = extract_news(item['url'])
            item['full_news'] = full_text
        except Exception as e:
            print(f"Error extracting news {i}: {e}")
            continue
    return news_list
```

### 6. 使用ChatGPT进行情感分析与投资建议

现在我们有了**完整新闻**。下面使用 **LangChain** + **OpenAI** 进行情感分析。

```python
import os
import openai
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI

openai.api_key = os.getenv("OPENAI_API_KEY")

# 初始化 ChatGPT 对话模型（这里示例使用gpt-4，可替换为其他模型）
chat = ChatOpenAI(model='gpt-4')

NEWS_ANALYSIS_PROMPT = """
You are an expert financial analyst. 
I will provide you with a list of news articles related to a stock. For each article:
1. Determine sentiment: Positive, Negative, or Neutral.
2. Summarize key points relevant to the stock.
3. Provide an overall summary of all articles and a final investment recommendation.

Format your output as:
{
  "sentiment_analysis": {
    "title1": "Positive",
    "title2": "Negative",
    ...
  },
  "key_points": [
    "...",
    "..."
  ],
  "overall_summary": "...",
  "recommendation": "..."
}
"""

def analyze_news_with_chatgpt(stock: str):
    # 获取并提取完整新闻
    news_data = extract_full_news(stock)
    
    # 拼接新闻到prompt
    articles_text = "\n\n".join([
        f"Title: {n['title']}\nContent: {n['full_news']}" for n in news_data if 'full_news' in n
    ])

    system_msg = SystemMessage(content=NEWS_ANALYSIS_PROMPT)
    user_msg = HumanMessage(content=f"Stock: {stock}\nNews:\n{articles_text}")

    response = chat([system_msg, user_msg])
    return response.content
```

调用方式示例：

```python
# result = analyze_news_with_chatgpt("AAPL")
# print(result)
```

ChatGPT将输出一个JSON结构，包含各新闻的情感判断、主要看点、整体总结及投资建议。你可以将此结果再解析并集成到前面构建的工作流中，实现**消息面 + 技术面 + 基本面**的三位一体代理分析。

---

## 总结与未来扩展

在本教程中，我们分两大部分展示了如何：

1. **使用DeepSeek-R1** 打造股票分析代理：  
   - 获取股价与技术指标  
   - 获取财务数据  
   - 使用LangGraph编排流程，生成可读分析报告  

2. **使用ChatGPT** 进行新闻内容分析代理：  
   - 获取与股票相关的新闻链接  
   - 提取网页正文并清洗  
   - 情感分析与投资建议输出  

### 你可以进一步做什么？

- **多Agent融合**：将“股票分析代理”与“新闻分析代理”合并到一个LangGraph工作流中，输出同时包含**股价、财务、新闻**的综合性分析。
- **强化因子模型**：根据行情特性，加入行业对比、宏观经济数据等更多因子。  
- **可视化与自动化**：把分析结果部署在Web界面或自动化任务流中，定时生成分析报告。  
- **换用其他开源大模型**：如BLOOM、LLaMA、ChatGLM等，比较分析效果和性能差异。  

> **无论是DeepSeek-R1还是ChatGPT，都可以根据实际需求进行灵活替换或互补**。希望本教程能够帮助你快速上手并搭建出自己的“代理型金融分析师”，在激烈的市场中获得更多洞察与机会。

如果你对相关代码有疑问或想分享更多想法，欢迎在评论区讨论。**让我们一起挖掘大模型在金融市场中的更多可能性！**

## 关于LLMQuant

LLMQuant是由一群来自世界顶尖高校和量化金融从业人员组成的前沿社区，致力于探索人工智能（AI）与量化（Quant）领域的无限可能。我们的团队成员来自剑桥大学、牛津大学、哈佛大学、苏黎世联邦理工学院、北京大学、中科大等世界知名高校，外部顾问来自Microsoft、HSBC、Citadel、Man Group、Citi、Jump Trading、国内顶尖私募

> [!note] 私募
> 向特定投资者（如对冲基金

> [!note] 对冲基金
> 采用多种策略（包括杠杆、卖空等）的投资基金
、银行）非公开发行证券
等一流企业。

