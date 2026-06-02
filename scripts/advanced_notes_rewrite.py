from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WIKI_ROOT = ROOT / "quant-wiki-notes"
TARGET_ROOT = WIKI_ROOT / "进阶专题"
TODAY = "2026-06-02"


INVALID_LINK_PREFIXES = (
    '"',
    "'",
)


TOPIC_LINKS = {
    "ETF投资体系": ["ETF产品分类与特征", "ETF资产配置优势与选择要点", "风险度量指标", "回测质量门清单"],
    "K线形态": ["技术分析完整指南", "量价关系与K线验证", "假形态识别与应对", "风险度量指标"],
    "估值方法": ["DCF现金流折现模型", "安全边际", "财务报告质量光谱", "风险度量指标"],
    "宏观经济分析": ["宏观经济分析框架总览", "资产配置入门", "固定收益与利率", "风险度量指标"],
    "回测方法": ["回测质量门清单", "前视偏差与幸存者偏差", "过拟合识别与防御", "市场微观结构与交易执行"],
    "机器学习交易": ["因子检验与评价", "过拟合识别与防御", "机器学习算法全景", "回测质量门清单"],
    "基本面分析": ["三大财务报表概览", "财务报告质量光谱", "安全边际", "估值指标体系"],
    "技术指标": ["技术分析完整指南", "量价关系与成交量指标", "假形态识别与应对", "风险度量指标"],
    "价值投资经典": ["安全边际", "巴菲特价值投资核心原则", "资产配置入门", "交易心理纪律"],
    "凯利公式与仓位管理": ["凯利公式概述", "仓位管理概述", "风险度量指标", "黑天鹅风险管理"],
    "可转债投资": ["可转债核心概念", "固定收益与利率", "市场微观结构与交易执行", "风险度量指标"],
    "量化部署": ["量化四大支柱", "从零搭建量化交易系统", "市场微观结构与交易执行", "Python量化环境配置"],
    "量化策略": ["量化投资完全指南", "回测质量门清单", "市场微观结构与交易执行", "量化风险管理体系"],
    "量化工具": ["Python量化环境配置", "AKShare概览", "VnPy框架详解", "量化数据源"],
    "期权策略": ["期权基础概念", "希腊字母总览", "期权Greeks风控", "风险度量指标"],
    "投资经典书单": ["安全边际", "巴菲特价值投资核心原则", "桥水基金原则", "交易心理纪律"],
    "行为金融学": ["行为金融学总览", "交易心理纪律", "量化策略解决心理问题", "风险度量指标"],
    "因子投资": ["因子投资总览", "因子检验与评价", "因子构建方法", "回测质量门清单"],
    "组合管理": ["现代投资组合理论", "风险度量指标", "量化风险管理体系", "资产配置入门"],
    "补充概念": ["进阶专题/目录", "量化投资完全指南", "回测质量门清单", "风险度量指标"],
}


TOPIC_GUIDANCE = {
    "ETF投资体系": {
        "positioning": "用 ETF 把大类资产、行业主题和策略工具模块化，重点不是猜单只产品，而是把指数暴露、费率、流动性和再平衡纪律放进同一张决策表。",
        "checks": ["底层指数是否清楚", "规模与成交额是否足以承载仓位", "跟踪误差和折溢价是否可接受", "是否有清晰的再平衡和止盈规则"],
        "risk": ["主题拥挤后估值回撤", "小规模 ETF 流动性不足", "跨境 ETF 汇率与时差风险", "杠杆/反向产品路径依赖"],
    },
    "K线形态": {
        "positioning": "K线只描述价格行为，不单独构成交易系统；必须与趋势级别、成交量、波动率和止损规则一起使用。",
        "checks": ["形态是否出现在关键位置", "成交量是否确认", "信号是否有统计样本支持", "止损点是否先于入场确定"],
        "risk": ["把形态当确定预测", "忽略大级别趋势", "假突破和诱多诱空", "频繁交易导致成本吞噬"],
    },
    "估值方法": {
        "positioning": "估值是给未来现金流定价，不是寻找精确数字；优秀交易者关注区间、假设弹性和安全边际。",
        "checks": ["核心假设是否可解释", "折现率/增长率是否做敏感性分析", "是否与行业可比公司交叉验证", "是否考虑资本周期和会计质量"],
        "risk": ["用单点估值制造虚假确定性", "忽略周期高点利润", "把低估值误认为低风险", "现金流口径前后不一致"],
    },
    "宏观经济分析": {
        "positioning": "宏观分析服务于资产配置和风险预算，重点看边际变化、预期差、政策反应函数和跨资产传导。",
        "checks": ["指标是领先、同步还是滞后", "市场一致预期是什么", "政策变量如何影响利率和风险偏好", "传导到哪类资产最直接"],
        "risk": ["用宏观结论直接择单票", "把长期判断用于短线交易", "忽视汇率和流动性约束", "把政策口号当已兑现业绩"],
    },
    "回测方法": {
        "positioning": "回测的首要任务是证伪策略，而不是证明策略赚钱；可靠回测必须同时处理数据、时间、成本、容量和风控。",
        "checks": ["是否使用 point-in-time 数据", "信号是否滞后一根 bar 执行", "手续费/滑点/冲击成本是否计入", "样本外和 walk-forward 是否通过"],
        "risk": ["前视偏差", "幸存者偏差", "参数过拟合", "实盘容量与流动性不足"],
    },
    "机器学习交易": {
        "positioning": "机器学习在交易中是预测和排序工具，不是收益机器；关键在数据切分、特征稳定性、可解释性和上线监控。",
        "checks": ["训练/验证/测试是否按时间切分", "特征是否可在交易时点获得", "收益标签是否扣成本", "模型漂移是否有监控"],
        "risk": ["随机切分造成泄漏", "高维特征过拟合", "黑箱模型难以风控", "训练收益无法覆盖交易成本"],
    },
    "基本面分析": {
        "positioning": "基本面研究把企业经营翻译成可验证的现金流、盈利质量和资本回报，最终落到估值和仓位。",
        "checks": ["收入和利润是否可持续", "现金流是否支持利润", "ROE 来自效率还是杠杆", "估值是否包含足够安全边际"],
        "risk": ["财报粉饰", "周期顶部外推", "只看利润不看现金流", "忽视治理和资本开支压力"],
    },
    "技术指标": {
        "positioning": "技术指标是价格与成交量的压缩表达，适合做信号过滤、风险控制和交易纪律，不适合孤立预测未来。",
        "checks": ["指标参数是否符合交易周期", "信号是否经过样本外验证", "是否与趋势/量能/波动率共振", "是否明确无效条件"],
        "risk": ["指标共线导致虚假确认", "震荡市和趋势市参数错配", "过度优化", "忽略滑点和交易成本"],
    },
    "价值投资经典": {
        "positioning": "经典投资思想的价值在于建立决策原则：能力圈、安全边际、长期复利、反身性和风险控制，而不是照搬大师持仓。",
        "checks": ["企业是否在能力圈内", "安全边际来自估值还是质量", "持有逻辑是否可被证伪", "仓位是否匹配不确定性"],
        "risk": ["把名人语录当交易信号", "长期主义掩盖错误", "低估值陷阱", "忽视组合层面的回撤"],
    },
    "凯利公式与仓位管理": {
        "positioning": "仓位管理解决的是在不确定世界中活得足够久；凯利公式提供上限，实盘通常用分数凯利和风险预算。",
        "checks": ["胜率和赔率是否有稳定样本", "最大亏损是否可承受", "相关仓位是否合并计算", "连续亏损时是否自动降杠杆"],
        "risk": ["高估胜率", "忽略尾部风险", "相关性在危机中上升", "满凯利导致心理和资金双重崩溃"],
    },
    "可转债投资": {
        "positioning": "可转债同时有债性、股性和条款博弈，分析必须把债底、转股价值、溢价率、信用风险和强赎风险放在一起。",
        "checks": ["债底和 YTM 是否合理", "转股溢价率是否过高", "正股弹性和信用质量如何", "强赎/回售/下修条款是否触发临界"],
        "risk": ["信用下沉", "高价高溢价双杀", "流动性薄导致滑点", "强赎前追高"],
    },
    "量化部署": {
        "positioning": "部署阶段把研究结果变成生产系统，核心是数据可靠、订单可追踪、风控可熔断、异常可恢复。",
        "checks": ["研究环境与实盘数据口径是否一致", "订单状态机是否完整", "风控是否前置", "日志、告警和回滚是否可用"],
        "risk": ["接口限频和断连", "重复下单", "数据延迟", "风控只在事后统计"],
    },
    "量化策略": {
        "positioning": "量化策略是投资假设、数据工程、回测验证、风险预算和执行系统的组合，不是单一公式。",
        "checks": ["假设是否可证伪", "数据是否 point-in-time", "绩效是否扣除真实成本", "上线后是否监控衰减"],
        "risk": ["数据挖掘偏差", "因子拥挤", "换手过高", "实盘偏离回测"],
    },
    "量化工具": {
        "positioning": "工具服务于研究闭环：获取数据、清洗数据、验证策略、执行交易和复盘监控；选择工具要看稳定性和可维护性。",
        "checks": ["接口是否稳定", "数据字段和频率是否满足策略", "版本是否锁定", "是否有替代数据源交叉验证"],
        "risk": ["免费数据缺口", "网页结构变化导致接口失效", "版本升级破坏兼容", "忽视数据授权和合规"],
    },
    "期权策略": {
        "positioning": "期权交易的是方向、波动率、时间价值和尾部风险的组合；必须先理解 Greeks 再谈策略收益。",
        "checks": ["Delta/Gamma/Vega/Theta 暴露是否清楚", "隐含波动率相对历史波动率如何", "保证金和极端情景是否测算", "到期与流动性是否匹配"],
        "risk": ["卖方尾部亏损", "波动率跳变", "流动性枯竭", "保证金追加"],
    },
    "投资经典书单": {
        "positioning": "书单的目标不是收藏观点，而是把经典框架转化成可执行的研究清单、交易纪律和复盘模板。",
        "checks": ["每本书解决什么问题", "能否转化为一条检查清单", "与自己的市场和周期是否匹配", "是否有反例验证"],
        "risk": ["只记结论不看前提", "过度崇拜单一大师", "忽视市场制度差异", "读书替代实证检验"],
    },
    "行为金融学": {
        "positioning": "行为金融学解释人为什么会系统性犯错；交易中的价值在于把偏误变成流程约束和反向观察指标。",
        "checks": ["当前决策受哪种偏误影响", "是否有预设退出规则", "是否用数据替代情绪判断", "复盘是否记录当时心理状态"],
        "risk": ["知道偏误但不改变流程", "逆向交易过早", "把市场情绪当必然反转", "亏损后加仓摊平"],
    },
    "因子投资": {
        "positioning": "因子投资把可解释的收益来源系统化，关键是因子定义、数据口径、检验方法、组合构建和衰减监控。",
        "checks": ["因子方向是否有经济解释", "是否做去极值/中性化/标准化", "IC 和分层收益是否稳定", "换手和容量是否可交易"],
        "risk": ["因子动物园", "样本内挖掘", "拥挤交易", "行业和市值暴露伪装成 alpha"],
    },
    "组合管理": {
        "positioning": "组合管理把单个机会变成可长期复利的资金曲线，核心是相关性、风险预算、再平衡和极端情景。",
        "checks": ["收益来源是否足够分散", "相关性在压力期如何变化", "再平衡规则是否机械执行", "最大回撤是否在承受范围内"],
        "risk": ["表面分散实则同一风险", "低估相关性突变", "杠杆叠加", "回撤期停止执行纪律"],
    },
    "补充概念": {
        "positioning": "补充概念是学习路径里的连接点：它不一定单独构成策略，但能帮助你把宏观、估值、因子、风控和执行串起来。",
        "checks": ["能否用一句话说明它解决什么问题", "它影响收益、风险、成本、流动性还是心理纪律", "它依赖哪些市场制度、数据口径或会计口径", "它应该连接到哪一个研究、交易或复盘动作"],
        "risk": ["只背术语不理解前提", "把概念名称误当交易信号", "忽略市场制度和数据口径差异", "没有验证就直接用于仓位决策"],
        "flow": [
            "先写出定义、反例和适用边界，避免把名词当结论。",
            "确认它连接的上游变量：宏观、财报、价格、成交量、订单簿、资金流或投资者行为。",
            "确认它影响的下游决策：选股、择时、仓位、对冲、执行、复盘或风控。",
            "找一个真实案例或历史区间，把概念落到数据、图表或交易记录上。",
            "把失效条件写进检查清单，避免在亏损后临时解释。",
        ],
    },
}


CORE_CONCEPTS = {
    "安全边际": {
        "aliases": ["Margin of Safety"],
        "body": "安全边际是估计价值与买入价格之间的缓冲区，用来吸收估值误差、经营波动和市场情绪冲击。实战中不要把它理解成单纯的低 PE，而要同时看资产质量、现金流稳定性、资产负债表强度和下行情景。",
        "steps": ["先估出保守价值区间", "用悲观假设重算现金流或清算价值", "只在价格明显低于保守价值时行动", "把仓位与不确定性反向挂钩"],
    },
    "Python量化环境配置": {
        "aliases": ["Python Quant Environment"],
        "body": "量化环境配置的目标是让研究可复现：固定 Python 版本、依赖版本、数据目录、时区和随机种子。真实项目不要依赖全局环境，建议使用虚拟环境、requirements/lock 文件和独立数据缓存。",
        "steps": ["创建虚拟环境", "锁定 numpy/pandas/scipy/statsmodels 等核心依赖", "记录数据下载日期和供应商", "用最小样例验证回测与绘图"],
    },
    "桥水基金原则": {
        "aliases": ["Bridgewater Principles"],
        "body": "桥水原则的投资含义是把观点、风险和流程显性化：先定义宏观机器如何运转，再通过风险平价、场景分散和严格复盘降低单一判断失误的破坏力。",
        "steps": ["把投资假设写成可检验命题", "区分增长与通胀两条主轴", "用风险贡献而非资金比例衡量分散", "定期复盘假设是否失效"],
    },
    "量化数据源": {
        "aliases": ["Quant Data Sources"],
        "body": "量化数据源决定策略上限。免费数据适合学习和原型验证，生产研究需要关注 point-in-time、退市样本、复权口径、公告日、延迟和授权。",
        "steps": ["先列出策略需要的字段和频率", "验证时间戳和复权逻辑", "用两个来源抽样交叉检查", "把数据版本写入回测报告"],
    },
    "量化系统架构": {
        "aliases": ["Quant System Architecture"],
        "body": "量化系统架构通常分为数据层、研究层、回测层、风控层、交易执行层和监控层。优秀架构的标准不是复杂，而是每一笔信号、订单和成交都能追溯。",
        "steps": ["统一证券主数据和交易日历", "把研究信号与订单执行解耦", "风控前置到下单前", "保存日志以支持盘后复盘"],
    },
    "市场微观结构与交易执行": {
        "aliases": ["Market Microstructure", "交易执行"],
        "body": "市场微观结构研究订单簿、买卖价差、成交机制、冲击成本和交易者行为。它决定纸面 alpha 能否变成真实收益，尤其影响高换手、套利、ETF、可转债和期权策略。",
        "steps": ["先看最小报价单位和撮合规则", "估计买卖价差与盘口深度", "用限价/分拆/TWAP 降低冲击", "用实盘成交回报校准滑点模型"],
    },
    "固定收益与利率": {
        "aliases": ["Fixed Income", "Interest Rates"],
        "body": "固定收益分析围绕现金流、久期、凸性、信用利差和收益率曲线展开。它不仅用于债券，也用于可转债债底、DCF 折现率、资产配置和宏观周期判断。",
        "steps": ["拆分无风险利率与信用利差", "计算久期和凸性", "观察收益率曲线形态", "把利率情景映射到股债商品配置"],
    },
    "资产配置入门": {
        "aliases": ["Asset Allocation"],
        "body": "资产配置解决的是跨资产的风险分散与长期复利问题。它要求把股票、债券、商品、现金、黄金和另类资产放在同一风险预算中比较。",
        "steps": ["定义投资期限和回撤承受能力", "选择低相关资产", "设定目标权重和再平衡频率", "用压力测试检查极端情景"],
    },
}


@dataclass
class NoteParts:
    frontmatter: str
    body: str
    had_frontmatter: bool


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def split_frontmatter(text: str) -> NoteParts:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return NoteParts(text[4:end], text[end + 5 :].lstrip("\n"), True)
    return NoteParts("", text.lstrip("\n"), False)


def first_h1(body: str) -> str | None:
    in_fence = False
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("# "):
            return line[2:].strip()
    return None


def count_real_h1(body: str) -> int:
    in_fence = False
    count = 0
    for line in body.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("# "):
            count += 1
    return count


def infer_title(path: Path, body: str, fm: str) -> str:
    h1 = first_h1(body)
    if h1:
        return clean_title(h1)
    m = re.search(r"(?m)^title:\s*['\"]?(.+?)['\"]?\s*$", fm)
    if m:
        return clean_title(m.group(1))
    return clean_title(path.stem)


def clean_title(title: str) -> str:
    title = title.strip()
    title = re.sub(r"^[#\s]+", "", title)
    title = title.strip('"').strip("'").strip()
    return title or "未命名"


def top_topic(path: Path) -> str:
    rel = path.relative_to(TARGET_ROOT)
    return rel.parts[0] if len(rel.parts) > 1 else "进阶专题"


def ensure_frontmatter(path: Path, parts: NoteParts, title: str) -> str:
    fm = parts.frontmatter.strip("\n")
    topic = top_topic(path)
    lines = fm.splitlines() if fm else []
    text = "\n".join(lines)

    def has_key(key: str) -> bool:
        return re.search(rf"(?m)^{re.escape(key)}\s*:", text) is not None

    if not has_key("title"):
        lines.insert(0, f"title: {title}")
    if not has_key("aliases"):
        lines.append("aliases: []")
    if not has_key("tags"):
        lines.extend(["tags:", "  - 进阶专题", f"  - {topic}"])
    if not has_key("created"):
        lines.append(f"created: {TODAY}")
    if not has_key("updated"):
        lines.append(f"updated: {TODAY}")
    if not has_key("source"):
        lines.append("source: 多源综合")
    return "---\n" + "\n".join(lines).strip() + "\n---\n\n"


def normalize_h1(body: str, title: str) -> str:
    lines = body.splitlines()
    out: list[str] = []
    in_fence = False
    seen_h1 = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if not in_fence and line.startswith("# "):
            if not seen_h1:
                out.append(line)
                seen_h1 = True
            else:
                out.append("#" + line)
            continue
        out.append(line)
    result = "\n".join(out).lstrip("\n")
    if not seen_h1:
        result = f"# {title}\n\n" + result
    return result


def fence_balanced(text: str) -> bool:
    return len(re.findall(r"(?m)^```", text)) % 2 == 0


def close_unbalanced_fence(text: str) -> str:
    if fence_balanced(text):
        return text
    return text.rstrip() + "\n```\n"


def topic_enhancement(path: Path) -> str:
    topic = top_topic(path)
    guide = TOPIC_GUIDANCE.get(topic, TOPIC_GUIDANCE["量化策略"])
    links = TOPIC_LINKS.get(topic, TOPIC_LINKS["量化策略"])
    checks = "\n".join(f"- {item}" for item in guide["checks"])
    risks = "\n".join(f"- {item}" for item in guide["risk"])
    link_lines = "\n".join(f"- [[{link}]]" for link in links)
    default_flow = [
        "先写清楚你的投资假设：为什么这个信号、资产或方法应该产生收益。",
        "明确数据口径：样本范围、更新时间、复权/分红/停牌处理和交易日历。",
        "做最小可行验证：先用简单规则验证方向，再逐步加入复杂模型。",
        "把成本和约束前置：手续费、滑点、冲击成本、保证金、流动性和容量都要进入测算。",
        "上线后持续复盘：记录信号、下单、成交、持仓、回撤和失效原因。",
    ]
    flow = "\n".join(f"{idx}. {item}" for idx, item in enumerate(guide.get("flow", default_flow), start=1))
    return f"""
## 课程化学习补充

> [!important] 学习定位
> {guide["positioning"]}本文仅用于学习、研究与复盘，不构成任何投资建议。

### 必须掌握的问题

{checks}

### 实战应用流程

{flow}

### 风险与失效条件

{risks}

### 复盘问题

- 这笔交易或这套模型赚的是什么钱：风险补偿、行为偏差、流动性溢价，还是偶然噪音？
- 如果市场环境反过来，最大亏损和最长恢复期会是多少？
- 当前结论是否依赖某个不可持续假设，例如低利率、低波动、充裕流动性或监管套利？
- 有没有一个更简单的基准策略能取得接近效果？

### 延伸学习

{link_lines}
""".strip()


def ensure_enhancement(body: str, path: Path) -> str:
    marker = "\n## 课程化学习补充\n"
    if "## 课程化学习补充" in body:
        if top_topic(path) == "补充概念" and "量化策略是投资假设、数据工程" in body:
            before, _, _ = body.partition(marker)
            return before.rstrip() + "\n\n" + topic_enhancement(path)
        return body
    return body.rstrip() + "\n\n" + topic_enhancement(path)


def fix_known_text(text: str) -> str:
    replacements = {
        "适度宽送": "适度宽松",
        "41.1k": "41.2k",
        "v1.18.63": "v1.18.64",
        "- **微信交流群**: 扫码添加小助手\n": "",
        "| 社区规模 | 41.1k⭐ | 14k⭐ | 17k⭐ |": "| 社区规模 | 41.2k⭐ | 14k⭐ | 17k⭐ |",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def normalize_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        raw = match.group(1)
        if raw.startswith(INVALID_LINK_PREFIXES):
            return "`" + raw.strip("`") + "`"
        target, alias = split_link(raw)
        cleaned_target = target.strip().replace("\\", "/")
        if cleaned_target.endswith("/"):
            cleaned_target = cleaned_target.rstrip("/") + "/目录"
        if cleaned_target.startswith("../量化投资/量化投资入门"):
            cleaned_target = "量化投资完全指南"
        elif cleaned_target.startswith("../技术分析/技术分析基础"):
            cleaned_target = "技术分析完整指南"
        elif cleaned_target.startswith("../价值投资/价值投资核心原则"):
            cleaned_target = "巴菲特价值投资核心原则"
        elif cleaned_target.endswith("/"):
            cleaned_target = cleaned_target.rstrip("/")
        cleaned_target = cleaned_target.rstrip("\\/")
        if not cleaned_target:
            return match.group(0)
        if alias:
            return f"[[{cleaned_target}|{alias}]]"
        return f"[[{cleaned_target}]]"

    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)


def split_link(raw: str) -> tuple[str, str | None]:
    if "|" in raw:
        target, alias = raw.split("|", 1)
        return target, alias
    return raw, None


def rewrite_note(path: Path) -> bool:
    original = read_text(path)
    text = fix_known_text(normalize_links(original))
    parts = split_frontmatter(text)
    title = infer_title(path, parts.body, parts.frontmatter)
    fm = ensure_frontmatter(path, parts, title)
    body = normalize_h1(parts.body, title)
    body = close_unbalanced_fence(body)
    if path.name != "目录.md":
        body = ensure_enhancement(body, path)
    new = fm + body
    new = re.sub(r"[ \t]+$", "", new, flags=re.MULTILINE).rstrip() + "\n"
    if new != original:
        write_text(path, new)
        return True
    return False


def make_root_index() -> None:
    content = """---
title: 进阶专题总览
aliases: [进阶专题, 投资交易进阶课程]
tags:
  - 进阶专题
  - 课程地图
  - 投资交易
created: 2026-06-02
updated: 2026-06-02
source: 多源综合
---

# 进阶专题总览

> [!note] 学习定位
> 本目录把进阶专题组织成一条完整的投资交易学习路径：先建立宏观与资产配置框架，再学习企业分析、估值、技术分析、行为金融、因子与量化策略，最后进入回测、组合管理、衍生品、工具与实盘部署。所有内容仅用于学习、研究与复盘，不构成投资建议。

## 一、学习路径

| 阶段 | 主题 | 先学什么 | 学完能做什么 |
|---|---|---|---|
| 1 | 宏观与资产配置 | [[宏观经济分析/目录|宏观经济分析]]、[[资产配置入门]]、[[固定收益与利率]] | 判断大类资产环境，形成风险预算 |
| 2 | 企业与估值 | [[基本面分析/目录|基本面分析]]、[[估值方法/目录|估值方法]]、[[安全边际]] | 读懂财报、估算价值、识别低估陷阱 |
| 3 | 技术与行为 | [[技术指标/目录|技术指标]]、[[K线形态/目录|K线形态]]、[[行为金融学/行为金融学总览|行为金融学]] | 用价格行为和心理偏差辅助交易纪律 |
| 4 | 因子与策略 | [[因子投资/目录|因子投资]]、[[量化策略/目录|量化策略]]、[[机器学习交易/目录|机器学习交易]] | 构建可检验的 Alpha 假设与策略原型 |
| 5 | 验证与风控 | [[回测方法/目录|回测方法]]、[[组合管理/目录|组合管理]]、[[凯利公式与仓位管理/凯利公式与仓位管理|凯利与仓位]] | 评估回撤、容量、成本和组合风险 |
| 6 | 工具与实盘 | [[量化工具/目录|量化工具]]、[[量化部署/目录|量化部署]]、[[市场微观结构与交易执行]] | 从研究环境走向可监控的交易系统 |
| 7 | 专项资产 | [[期权策略/目录|期权策略]]、[[可转债投资/目录|可转债投资]]、[[ETF投资体系/目录|ETF投资体系]] | 理解衍生品、转债和 ETF 的专门风险 |
| 8 | 思维模型 | [[价值投资经典/目录|价值投资经典]]、[[投资经典书单/目录|投资经典书单]] | 把大师经验转成自己的检查清单 |

## 二、交易者实战框架

1. **先问收益来源**：这笔钱来自风险补偿、行为偏差、流动性溢价、制度约束，还是统计噪音？
2. **再问数据是否真实可得**：财报公告日、退市样本、复权、停牌、交易成本和滑点必须进入研究。
3. **然后做可证伪回测**：策略应先经受前视偏差、幸存者偏差、过拟合和样本外测试。
4. **最后决定仓位**：用最大回撤、相关性、流动性和极端情景决定能投多少钱，而不是只看收益率。

## 三、时效资料核验记录

截至 2026-06-02，本轮改写对时效性内容采用官方或项目源交叉核验：

| 主题 | 核验结论 | 来源 |
|---|---|---|
| AKShare | PyPI 显示最新版本为 1.18.64，上传日期 2026-05-27 | [PyPI akshare](https://pypi.org/project/akshare/) |
| VeighNa/vnpy | GitHub 显示 4.4.0 为 Latest Release，日期 2026-05-14，约 41.2k stars | [vnpy/vnpy](https://github.com/vnpy/vnpy) |
| 上交所交易规则 | 《上海证券交易所交易规则（2026年修订）》发布于 2026-04-24，生效日为 2026-07-06 | [上海证券交易所](https://www.sse.com.cn/lawandrules/sselawsrules2025/trade/universal/c/c_20260424_10816492.shtml) |
| 美联储政策框架 | 2025 年框架评估强调 2% 通胀目标未改变，并约每五年做公开评估 | [Federal Reserve](https://www.federalreserve.gov/monetarypolicy/review-of-monetary-policy-strategy-tools-and-communications-qas-2025.htm) |
| 程序化交易监管 | 证券市场程序化交易自 2024-10-08 起实施；期货市场程序化交易管理规定自 2025-10-09 起实施 | [证券市场规定](https://www.csrc.gov.cn/csrc/c100028/c7480577/content.shtml)、[期货市场规定](https://www.csrc.gov.cn/csrc/c100028/c7564353/content.shtml) |

## 四、核心入口

- [[宏观经济分析/目录|宏观经济分析]]
- [[基本面分析/目录|基本面分析]]
- [[估值方法/目录|估值方法]]
- [[技术指标/目录|技术指标]]
- [[K线形态/目录|K线形态]]
- [[因子投资/目录|因子投资]]
- [[量化策略/目录|量化策略]]
- [[回测方法/目录|回测方法]]
- [[组合管理/目录|组合管理]]
- [[期权策略/目录|期权策略]]
- [[可转债投资/目录|可转债投资]]
- [[ETF投资体系/目录|ETF投资体系]]
- [[量化工具/目录|量化工具]]
- [[量化部署/目录|量化部署]]
"""
    write_text(TARGET_ROOT / "目录.md", content)


def make_directory_indexes() -> int:
    count = 0
    for directory in sorted([p for p in TARGET_ROOT.rglob("*") if p.is_dir()]):
        index = directory / "目录.md"
        if index.exists():
            continue
        notes = sorted(p for p in directory.glob("*.md") if p.name != "目录.md")
        subdirs = sorted(p for p in directory.iterdir() if p.is_dir())
        title = directory.name
        topic = directory.relative_to(TARGET_ROOT).parts[0]
        note_links = "\n".join(f"- [[{p.stem}]]" for p in notes) or "- 暂无直属笔记，先阅读下级目录。"
        subdir_links = "\n".join(f"- [[{p.name}/目录|{p.name}]]" for p in subdirs) or "- 无下级目录。"
        content = f"""---
title: {title}
aliases: [{title}目录]
tags:
  - 进阶专题
  - {topic}
  - 目录
created: {TODAY}
updated: {TODAY}
source: 自动整理
---

# {title}

> [!note] 学习定位
> 本目录用于连接 `{title}` 主题下的课程化笔记。建议先读总览，再按专题逐篇学习，最后回到实战清单复盘。

## 下级目录

{subdir_links}

## 直属笔记

{note_links}
"""
        write_text(index, content)
        count += 1
    return count


def concept_body(name: str) -> tuple[list[str], str, list[str]]:
    if name in CORE_CONCEPTS:
        data = CORE_CONCEPTS[name]
        return data["aliases"], data["body"], data["steps"]
    aliases: list[str] = []
    if "因子" in name:
        body = f"{name}用于把某类可观察特征转化为可排序、可检验的投资信号。实战中要同时关注经济解释、数据可得性、IC 稳定性、换手率和容量。"
        steps = ["定义清晰可复现的计算口径", "做去极值、标准化和中性化", "检验 IC、分层收益和换手", "上线后监控拥挤和衰减"]
    elif "估值" in name or name in {"PE", "PB", "PS", "ROE", "市盈率"}:
        body = f"{name}是估值或财务分析中的补充概念。使用时要明确分子分母、会计口径、行业差异和周期位置，避免用单一指标替代完整判断。"
        steps = ["明确指标定义", "与行业和历史分位比较", "做情景和敏感性分析", "结合现金流与资产负债表验证"]
    elif "交易" in name or "系统" in name or "接口" in name or "数据" in name:
        body = f"{name}属于量化工具与交易系统中的实践概念。重点是稳定性、可追踪性、合规性和出现异常时的恢复能力。"
        steps = ["明确输入输出和依赖", "记录版本与数据时间", "设置异常告警", "用小资金或仿真环境验证"]
    elif "巴菲特" in name or "芒格" in name or "达利欧" in name or "索罗斯" in name or "桥水" in name:
        body = f"{name}属于经典投资思想中的方法论概念。学习时要还原其前提、市场环境和风险约束，而不是直接复制结论或持仓。"
        steps = ["提炼核心原则", "写出适用和不适用场景", "转化为自己的检查清单", "用历史案例和反例复盘"]
    else:
        body = f"{name}是进阶专题中的补充概念，用于连接相关笔记、减少知识断点。学习时应先掌握定义，再理解适用场景、风险边界和可验证方法。"
        steps = ["先写出一句话定义", "找到可观察的数据或案例", "明确它影响收益还是风险", "把结论放入交易或研究清单"]
    return aliases, body, steps


def make_concept_note(name: str) -> str:
    aliases, body, steps = concept_body(name)
    alias_text = "[" + ", ".join(aliases) + "]" if aliases else "[]"
    step_text = "\n".join(f"{i}. {step}" for i, step in enumerate(steps, 1))
    return f"""---
title: {name}
aliases: {alias_text}
tags:
  - 进阶专题
  - 补充概念
  - 投资交易
created: {TODAY}
updated: {TODAY}
source: 课程化补充
---

# {name}

> [!note] 概念定位
> {body}

## 一、直觉解释

把 `{name}` 放进交易框架里，它通常回答三个问题：为什么这个现象存在、它会影响收益还是风险、在什么约束下会失效。不要只记名词，要能把它写成可执行的研究或交易规则。

## 二、实战检查

{step_text}

## 三、常见误区

- 只看概念名称，不核对计算口径或制度前提。
- 把历史规律当成未来保证，忽略样本外变化。
- 不计交易成本、滑点、税费、流动性和容量。
- 没有预先定义失效条件，亏损后才临时解释。

## 四、相关学习

- [[量化投资完全指南]]
- [[回测质量门清单]]
- [[风险度量指标]]
- [[市场微观结构与交易执行]]
"""


def existing_names() -> set[str]:
    return {p.stem for p in WIKI_ROOT.rglob("*.md")}


def parse_links(text: str) -> list[str]:
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def target_from_raw(raw: str) -> str:
    target, _ = split_link(raw)
    target = target.split("#", 1)[0].strip().replace("\\", "/").rstrip("/")
    if "/" in target:
        target = target.split("/")[-1]
    return target


def is_link_resolved(raw: str, names: set[str]) -> bool:
    target = target_from_raw(raw)
    if not target or target.startswith(INVALID_LINK_PREFIXES):
        return True
    return target in names


def create_missing_concepts() -> int:
    names = existing_names()
    missing: set[str] = set()
    for path in TARGET_ROOT.rglob("*.md"):
        text = read_text(path)
        for raw in parse_links(text):
            target = target_from_raw(raw)
            if not target or target.startswith(INVALID_LINK_PREFIXES):
                continue
            if target not in names:
                missing.add(target)
    concept_dir = TARGET_ROOT / "补充概念"
    count = 0
    for name in sorted(missing):
        if re.search(r'[<>:"/\\|?*]', name):
            continue
        path = concept_dir / f"{name}.md"
        if not path.exists():
            write_text(path, make_concept_note(name))
            count += 1
    return count


def write_manifest() -> None:
    rows = []
    for path in sorted(TARGET_ROOT.rglob("*.md")):
        text = read_text(path)
        parts = split_frontmatter(text)
        rows.append(
            {
                "path": str(path.relative_to(ROOT)).replace("\\", "/"),
                "lines": len(text.splitlines()),
                "h1": count_real_h1(parts.body),
                "has_frontmatter": parts.had_frontmatter,
                "links": len(parse_links(text)),
                "has_course_section": "## 课程化学习补充" in text,
                "fence_balanced": fence_balanced(text),
            }
        )
    report = TARGET_ROOT / "_课程化改写清单.json"
    write_text(report, json.dumps(rows, ensure_ascii=False, indent=2))


def main() -> None:
    make_root_index()
    created_indexes = make_directory_indexes()
    changed = 0
    for path in sorted(TARGET_ROOT.rglob("*.md")):
        if path.name == "_课程化改写清单.json":
            continue
        if rewrite_note(path):
            changed += 1
    created_concepts = create_missing_concepts()
    created_indexes += make_directory_indexes()
    for path in sorted(TARGET_ROOT.rglob("*.md")):
        rewrite_note(path)
    write_manifest()
    print(json.dumps({"changed": changed, "created_indexes": created_indexes, "created_concepts": created_concepts}, ensure_ascii=False))


if __name__ == "__main__":
    main()
