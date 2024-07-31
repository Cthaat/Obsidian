---
tags: vue , nuxt3
---

---

## 问题

 - 在nuxt3中使用$fetch获取不到数据
 - 原因是获取数据的时候没有使用await等待
 - 还没有获取数据就直接执行下边代码了
 - 下边代码使用该数据为空

---

## 解决

```javascript
const logout = async () => {

  const response = await $fetch('/api/user/logout');
```
