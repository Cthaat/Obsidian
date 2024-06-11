---
title: test
date: 2024-05-08
tags:
  - blog
  - Obsidian
  - good
aliases:
  - 别名
cssclasses: 
strings:
 - 123
 - Hello Dataview
---

```dataview
Table file.name AS 文件名 , file.ctime AS 创建时间 , file.mtiem AS 修改时间 , file.tags AS 标签
where file = this.file
FLATTEN genres
```

```dataview
TASK
WHERE start = date("2024-04-22")
```

# 主要内容

123

- [ ] 任务创建 [created:: 2024-04-25]
- [ ] 任务开始 [start:: 2024-04-26]
- [ ] 任务开始2 [start:: 2024-04-22]
- [ ] 任务完成
    - [ ] 子任务完成 1 
    - [ ] 子任务未完成 1
    - [ ] 子任务完成 2 [completion:: 2024-04-28]
- [x] 任务全部完成 ✅ 2024-06-11
    - [ ] 完成 1
    - [ ] 完成 2

```dataviewjs
let currentFilename = dv.current().file.name
dv.list([currentFilename])
```

```dataview
TABLE genres
FROM "test"
FLATTEN genres
```