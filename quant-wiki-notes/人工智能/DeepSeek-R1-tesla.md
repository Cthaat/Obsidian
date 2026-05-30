---
title: "深度解析：如何用DeepSeek-R1对特斯拉相关新闻进行情感分析并生成投资建议"
category: "AI+量化"
tags: [AI+量化, 量化, 投资, 金融]
source: "quant-wiki.com"
created: 2026-05-30
---

# 深度解析：如何用DeepSeek-R1对特斯拉相关新闻进行情感分析并生成投资建议

在股票投资中，**消息面**往往会对股价造成显著影响。实时监测并分析新闻资讯，有助于我们判断市场情绪并优化投资决策。本文以特斯拉（**TSLA**）为例，结合 **Yahoo Finance**、**MarkItDown** 和 **DeepSeek-R1** 模型，展示从“获取新闻→提取正文→情感分析→投资建议”的完整实践流程。

**适合人群**：对自动化金融资讯分析感兴趣的量化工程师、数据科学家、基金经理或想要快速上手新闻情感分析的学习者。

## 功能概览

1. **抓取特斯拉相关新闻**：利用 `yfinance` 获取 TSLA 最新新闻。
2. **提取并清洗正文**：使用 MarkItDown 库解析网页内容，并对文本做简单的正则清理。
3. **情感分析与建议**：基于 DeepSeek-R1 模型，对多篇新闻打分并输出投资建议。

通过这些步骤，你可以快速搭建一个多篇新闻合并分析的“小型舆情雷达”。

## 一、准备环境

1. 安装Python依赖：
   ```bash
   pip install yfinance pandas markitdown requests langchain langchain-ollama
   ```
2. 确保本地或服务器已成功部署 **DeepSeek-R1** 模型，并可通过 [Ollama](https://ollama.人工智能/) 或类似方式调用。

如果你还没有DeepSeek-R1模型，可以尝试在本地安装相应环境，或替换为其他兼容的模型。

---

## 二、获取特斯拉（TSLA）的相关新闻

### 2.1 编写 `get_news` 函数

以下函数通过 `yfinance` 库中的 `Ticker` 对象抓取特斯拉相关新闻，并提取关键字段（标题、摘要、链接、发布日期）：

```python
import yfinance as yf
import pandas as pd

def get_news(stock: str) -> list:
    """
    获取与指定股票相关的新闻列表，返回包含标题、摘要、链接、发布日期的字典列表。
    """
    try:
        # 获取股票对象及其新闻
        ticker = yf.Ticker(stock)
        news = ticker.news

        # 如果没有新闻，则返回空列表
        if not news:
            print(f"No news found for {stock}.")
            return []

        # 只保留contentType='STORY'的新闻
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

#### 示例调用

```python
news_list = get_news("TSLA")
print(len(news_list))  # 查看获取到的新闻数量
print(news_list[0])    # 输出其中一篇新闻的信息
```

获取到的结构如：

```python
{
    'title': 'Tesla Poised to Beat Q1 Earnings Estimates...',
    'summary': '...',
    'url': 'https://finance.yahoo.com/news/...',
    'pubdate': '2025-01-20'
}
```

## 三、提取并清洗新闻正文

### 3.1 使用 MarkItDown 解析网页

`MarkItDown` 可以帮助我们将网页HTML转换成纯文本，包括标题和正文内容。在提取文本的同时，我们会移除一些**链接**与**特殊字符**，使后续分析更干净。

```python
from markitdown import MarkItDown
import requests
import re

# 创建Session以提高稳定性
session = requests.Session()
session.headers.update({
    'User-Agent': 'python-requests/2.32.3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'keep-alive'
})
md = MarkItDown(requests_session=session)

def remove_links(text: str) -> str:
    """
    去除URL、Markdown格式链接及多余字符
    """
    text = re.sub(r'http\S+', '', text)       # 移除URL
    text = re.sub(r'\[.*?\]', '', text)       # 移除Markdown链接
    text = re.sub(r'[#*()+\-\n]', '', text)   # 移除特殊字符
    text = re.sub(r'/\S*', '', text)          # 移除带斜线的内容
    text = re.sub(r'  ', '', text)            # 移除多余空格
    return text

def extract_news(link: str) -> str:
    """
    基于MarkItDown抽取页面标题与正文，并进行清洗后返回。
    """
    info = md.convert(link)
    text_title = info.title.strip()
    text_content = info.text_content.strip()
    return text_title + '\n' + remove_links(text_content)
```

### 3.2 获取并整合所有新闻文本

有了 `get_news` 与 `extract_news`，我们可以一次性对所有新闻进行提取。示例如下：

```python
def extract_full_news(stock: str) -> list:
    """
    以full_news字段的形式，把网页正文添加到每篇新闻中返回。
    """
    news_data = get_news(stock)
    for i, item in enumerate(news_data):
        try:
            content = extract_news(item['url'])
            item['full_news'] = content
        except Exception as e:
            print(f"Error extracting news {i}: {e}")
            continue
    return news_data

# 以TSLA为例
full_news_list = extract_full_news("TSLA")

print(full_news_list[0]['title'])       # 新闻标题
print(full_news_list[0]['full_news'])   # 提取后的完整正文
```

得到的 `full_news_list` 即是包含所有字段（标题、摘要、URL、正文等）的整合结果。

![](https://fastly.jsdelivr.net/gh/bucketio/img5@main/2025/02/26/1740600002331-9d6ca907-4b79-48d9-bb67-94245f893670.png)

## 四、使用DeepSeek-R1进行情感分析与投资建议

### 4.1 DeepSeek-R1与LangChain绑定

本例使用 [OllamaLLM](https://pypi.org/project/langchain-ollama/) 作为调用DeepSeek-R1的接口。将多篇新闻合并后送入LLM做情感分析。

```python
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pprint import pprint

# 初始化DeepSeek-R1
llm = OllamaLLM(model="deepseek-r1:1.5b")
```

### 4.2 编写提示模板（Prompt）

我们希望模型逐条给出“Positive/Negative/Neutral”的情感评价，并结合所有文章总结后给出投资建议。可将需求写成`system`的提示，传给LLM：

```python
PROMPT = """
You are an expert financial analyst. I will provide you with a list of news articles related to Tesla (TSLA). Your tasks:

1. **Sentiment Analysis:**
   - For each news article, evaluate its sentiment as 'Positive', 'Negative', or 'Neutral'.
   - Present your evaluation in a dictionary format like: {"Article Title": "Positive", ...}

2. **Comprehensive Summary & Recommendation:**
   - Summarize the overall sentiment and key points from all articles.
   - Advise if investing in TSLA is advisable, with reasons derived from the news analysis.

**News Articles:**

{articles}

**Output Format:**

1. Sentiment Analysis Dictionary (JSON)
2. Summary
3. Investment Recommendation
"""

prompt_template = ChatPromptTemplate.from_messages(
    [
        ('system', PROMPT),
        ('human', "I want to analyze TSLA's news articles in detail.")
    ]
)
```

### 4.3 调用模型并输出结果

将我们提取的正文文本（`full_news`）组合为一个列表，作为 `articles` 传入 PromptTemplate，最后调用 LLM：

```python
structure = prompt_template | llm

result = structure.invoke({
    "articles": [item['full_news'] for item in full_news_list]
})

pprint(result)
```

当DeepSeek-R1完成生成后，你将看到类似如下结果：

```txt
"<think>\n... [模型内部推理] ...\n</think>\n\n
### Sentiment Analysis Dictionary
```json
{
   "Tesla Q4 Earnings: A Beat on Estimates?": "Positive",
   "Elon Musk's Latest Statement Sparks Controversy": "Neutral",
   ...
}
```
```

### Summary

Based on the articles, Tesla's expansion in Europe...

### Investment Recommendation

Tesla continues to demonstrate strong performance...
"
```

这些信息包括**逐篇情感打分**、**整体总结**以及**投资建议**，让我们对特斯拉近期新闻有了直观的认识，也为决策提供了更多参考。

---

## 五、更多进阶思路

1. **结合技术面与基本面**：你可以把本篇教程中获取的“新闻情绪”与股票的技术指标、财务指标相结合，构建一个多因子分析代理。
2. **自动化调度**：使用如 Airflow 或Cron定期执行此脚本，保持对最新新闻的跟踪；在得到结果后推送到自定义通知或可视化仪表盘。
3. **接入其他LLM或插件**：如果想尝试不同模型的分析效果，也可将DeepSeek-R1替换为其他如ChatGPT、LLaMA等，比较情感判断的准确率与速度。

---

## 结论

借助 **yfinance** 抓取特斯拉新闻、**MarkItDown** 提取网页正文，再通过 **DeepSeek-R1** 进行情感分析和投资建议生成，即可实现一个“**实时新闻舆情分析**”的简易雏形。
- **自动化**：可大规模、持续地抓取最新新闻。
- **可扩展**：可灵活替换模型或将结果进一步整合到更复杂的金融决策流程中。

通过上述步骤，可以形成从新闻数据获取、正文抽取到模型分析的完整流程。
