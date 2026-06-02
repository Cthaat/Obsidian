---
title: efinance 版本演进
tags: [efinance, 版本历史, Changelog]
created: 2026-06-02
source: /opt/data/investment/kb/doc-sites/efinance-数据/en_v*.md (24 files)
parent: "[[efinance概览]]"
---

# efinance 版本演进

> [!note] 版本轨迹
> efinance 从 **v0.3.3** 持续迭代至 **v0.5.8**（latest），共 24 个版本。稳定版为 v0.5.4。

## 版本时间线

| 版本 | 里程碑 |
|------|--------|
| v0.3.3 | 初始版本，支持股票基本功能 |
| v0.3.4 ~ v0.3.9 | 早期迭代，逐步完善 |
| v0.4.0 ~ v0.4.9 | 功能稳定期，增加实时行情等 |
| v0.5.0 ~ v0.5.4 | 重大版本更新（stable） |
| v0.5.5 ~ v0.5.8 | 最新版本（latest） |

## 主要版本变化

### v0.3.x 系列（初期）

- v0.3.3：首次发布，核心股票K线数据获取
- v0.3.4：修复数据源异常
- v0.3.5 ~ v0.3.9：增加更多股票接口，逐步添加基金支持

### v0.4.x 系列（稳定扩展）

- v0.4.0：重要版本，API 结构优化
- v0.4.2 ~ v0.4.4：bug 修复 + 性能优化
- v0.4.5 ~ v0.4.7：增加非A股支持（美股、港股）
- v0.4.8 ~ v0.4.9：期货数据模块引入

### v0.5.x 系列（当前主线）

- v0.5.0：模块化重构（`ef.stock` / `ef.fund` / `ef.futures`）
- v0.5.1：Docker 支持完善
- v0.5.2：实时行情功能增强
- v0.5.3：数据源可靠性提升
- **v0.5.4**：当前 **stable** 版本
- v0.5.5 ~ **v0.5.8**：持续迭代（latest）

## 版本使用建议

| 场景 | 推荐版本 | 原因 |
|------|---------|------|
| 生产环境 | v0.5.4 (stable) | 经过充分测试的稳定版 |
| 尝鲜体验 | v0.5.8 (latest) | 最新功能 |
| 新项目 | v0.5.4+ | 模块化 API，向后兼容 |

## 安装指定版本

```bash
# 安装稳定版
pip install efinance==0.5.4

# 安装最新版
pip install efinance --upgrade

# 查看已安装版本
python -c "import efinance; print(efinance.__version__)"
```

## 相关笔记
- [[efinance概览]]
- [[efinance-常用接口]]
