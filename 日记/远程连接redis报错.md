---
tags:
  - 数据库
  - docker
  - 虚拟机
  - redis
  - 错误
  - 已解决
---

## 概述

 - 错误
 - ![[Pasted image 20240614132807.png]]
 - 解决
 - ![[Pasted image 20240614133413.png]]
 - 在docker中重启服务成功连接

---

## 问题复现

- 重启虚拟机会再次遇到问题
- 然后ssh连接虚拟机输入密码后解决问题
- ![[Pasted image 20240614133832.png]]

---
## 问题变更

 - 未改变任何参数
 - 只要打开虚拟机就可以连接成功，不用虚拟机密码

---

## 深层原因

- 未知