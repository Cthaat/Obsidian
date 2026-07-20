# 张宇基础30讲全表格修复 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Completed steps use checked-box (`- [x]`) syntax for tracking.

**Goal:** 检查并修复 `考研数学/张宇基础30讲笔记` 下全部 Markdown 表格，使其在 Obsidian 中保持正确列结构与数学公式显示。

**Architecture:** 先用只读扫描器识别真实 Markdown 表格块，再检查每行结构分隔符、数学环境、Wiki 链接别名和行内代码中的原始竖线。按文件区间分批修复，只替换会破坏表格的语法，不改正文含义，最后对全部 40 个文件重新扫描。

**Tech Stack:** Markdown、Obsidian Wiki 链接、KaTeX、PowerShell、Git 差异检查

---

### Task 1: 建立全量失败基线

**Files:**
- Inspect: `考研数学/张宇基础30讲笔记/*.md`
- Preserve: `.obsidian/workspace.json`
- Preserve: `考研数学/错题/*.md`

- [x] **Step 1: 识别表格块**

以合法分隔行（例如 `|---|---|`）为锚点，向前取得表头、向后取得连续表格行，排除展示公式中以 `|` 开头的普通正文。

- [x] **Step 2: 扫描会破坏列结构的语法**

检查表格数学环境中的原始 `|`、Wiki 链接别名中的未转义 `|`、行内代码中的原始 `|`、不配对的 `$`，以及与分隔行不一致的列数。

- [x] **Step 3: 运行失败基线**

预期：命令以非零状态退出，并输出每个问题的文件、行号、问题类型和原始行。

### Task 2: 分批修复表格语法

**Files:**
- Modify when reported: `考研数学/张宇基础30讲笔记/00_*.md`
- Modify when reported: `考研数学/张宇基础30讲笔记/01_*.md` through `10_*.md`
- Modify when reported: `考研数学/张宇基础30讲笔记/11_*.md` through `20_*.md`, including `18A_*.md`
- Modify when reported: `考研数学/张宇基础30讲笔记/21_*.md` through `31_*.md`

- [x] **Step 1: 修复数学绝对值和条件竖线**

将表格数学公式中的绝对值改为 `\lvert...\rvert`，条件符号按语义改为 `\mid`，不改变公式含义。

- [x] **Step 2: 修复 Wiki 链接和行内代码分隔符**

表格中的 Wiki 链接别名使用 `[[目标\|别名]]`；确需显示的普通竖线使用 `\|`。

- [x] **Step 3: 修复真实列数异常**

根据表头和相邻同类行恢复缺失或多余单元格；不得靠删除内容绕过检查。

- [x] **Step 4: 每批运行定向检查**

每个文件区间修复后重新扫描该区间，预期问题数为 0，再进入下一批。

### Task 3: 全库复核与差异审查

**Files:**
- Verify: `考研数学/张宇基础30讲笔记/*.md`
- Review: all modified lecture and index Markdown files

- [x] **Step 1: 重新运行全量表格检查**

预期：全部表格行的列数与各自分隔行一致；数学、Wiki 链接和代码环境中没有未处理的原始竖线；行内数学定界符配对。

- [x] **Step 2: 检查 Markdown 结构**

验证每个讲义 H1 数量、反引号与波浪号代码围栏配对，并确认修改行中的 `\lvert`/`\rvert` 配对。

- [x] **Step 3: 运行 Git 校验**

运行 `git diff --check -- 考研数学/张宇基础30讲笔记`，预期退出码为 0。

- [x] **Step 4: 审查最终差异**

确认只修改表格语法与本计划文件，不覆盖用户的错题笔记或 Obsidian 工作区状态；不提交、不推送。
