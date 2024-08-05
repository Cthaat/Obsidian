---
tags: JavaWeb
---

---

## 概念

 - ![[Pasted image 20240804225321.png]]

---

## 快速入门

 - 创建
 - ![[Pasted image 20240804225340.png]]
 - 部署
 - ![[Pasted image 20240804225346.png]]
 - 执行原理
 - ![[Pasted image 20240804225356.png]]
 - ![[Pasted image 20240804225359.png]]

---

## 方法

 - 初始化
 - ![[Pasted image 20240804225435.png]]
 - ![[Pasted image 20240804225438.png]]
 - 提供服务
 - ![[Pasted image 20240804225449.png]]
 - ![[Pasted image 20240804225453.png]]
 - 销毁
 - ![[Pasted image 20240804225501.png]]
 - ![[Pasted image 20240804225504.png]]
 - 获取对象
 - ![[Pasted image 20240804225514.png]]
 - 获取信息
 - ![[Pasted image 20240804225526.png]]
 - 生命周期
 - ![[Pasted image 20240804225550.png]]
 - ![[Pasted image 20240804225553.png]]
 - ![[Pasted image 20240804225555.png]]
 - 3.0版本
 - ![[Pasted image 20240804225608.png]]
 - ![[Pasted image 20240804225611.png]]

---

## 体系结构

 - ![[Pasted image 20240804225626.png]]
 - GenericServlet
 - ![[Pasted image 20240804225634.png]]
 - HttpServlet
 - ![[Pasted image 20240804225643.png]]
 - ![[Pasted image 20240804225646.png]]
 - 相关配置
 - ![[Pasted image 20240804225657.png]]

---

## Request

- ![[Pasted image 20240804225719.png]]
- 概念
- ![[Pasted image 20240804225729.png]]
- 继承体系
- ![[Pasted image 20240804225735.png]]
- 功能
	- 获取请求行
	- ![[Pasted image 20240804225749.png]]
	- ![[Pasted image 20240804225752.png]]
	- 获取请求头
	- ![[Pasted image 20240804225800.png]]
	- ![[Pasted image 20240804225803.png]]
	- ![[Pasted image 20240804225805.png]]
	- ![[Pasted image 20240804225808.png]]
	- 获取请求体
	- ![[Pasted image 20240804225817.png]]
	- ![[Pasted image 20240804225820.png]]
	- ![[Pasted image 20240804225824.png]]
	- 获取请求参数
	- ![[Pasted image 20240804225837.png]]
	- ![[Pasted image 20240804225840.png]]
	- 中文乱码
	- ![[Pasted image 20240804225848.png]]
 - 请求转发
 - ![[Pasted image 20240804225921.png]]
 - ![[Pasted image 20240804225926.png]]
 - ServletContext
 - ![[Pasted image 20240804225939.png]]
 - 登陆案例
 - ![[Pasted image 20240804225949.png]]
 - 然后转发存储的用户名
 - 发送给登录成功或者登录失败的页面
 - JavaBean
 - ![[Pasted image 20240804230006.png]]
 - ![[Pasted image 20240804230016.png]]
 - ![[Pasted image 20240804230019.png]]

---

## Response

 - ![[Pasted image 20240804230036.png]]
 - ![[Pasted image 20240804230040.png]]
 - ![[Pasted image 20240804230044.png]]
 - 响应行
 - ![[Pasted image 20240804230052.png]]
 - 响应头
 - ![[Pasted image 20240804230100.png]]
 - 功能
	 - ![[Pasted image 20240804230107.png]]
	 - 重定向
	 - ![[Pasted image 20240804230122.png]]
	 - ![[Pasted image 20240804230125.png]]
	 - ![[Pasted image 20240804230129.png]]
	 - 路径
	 - ![[Pasted image 20240804230135.png]]
	 - ![[Pasted image 20240804230138.png]]
	 - 动态获取目录
	 - ![[Pasted image 20240804230146.png]]
	 - ![[Pasted image 20240804230150.png]]
	 - 输出流
	 - ![[Pasted image 20240804230201.png]]
	 - ![[Pasted image 20240804230204.png]]
	 - ![[Pasted image 20240804230208.png]]
	 - 验证码
	 - ![[Pasted image 20240804230218.png]]
	 - ![[Pasted image 20240804230221.png]]
	 - ![[Pasted image 20240804230225.png]]
	 - 点击切换
	 - ![[Pasted image 20240804230231.png]]

---

## ServletContext

 - 获取
 - ![[Pasted image 20240804230305.png]]
 - ![[Pasted image 20240804230308.png]]
 - 功能
	 - 获取MIME
	 - ![[Pasted image 20240804230321.png]]
	 - ![[Pasted image 20240804230324.png]]
	 - 共享数据
	 - ![[Pasted image 20240804230331.png]]
	 - 获取真实路径
	 - ![[Pasted image 20240804230338.png]]
	 - 文件下载
	 - ![[Pasted image 20240804230345.png]]
	 - ![[Pasted image 20240804230347.png]]
	 - ![[Pasted image 20240804230352.png]]
	 - 中文文件
	 - ![[Pasted image 20240804230359.png]]

---

## 会话技术

 - ![[Pasted image 20240804230420.png]]
 - Cookie
	 - 使用
	 - ![[Pasted image 20240804230430.png]]
	 - ![[Pasted image 20240804230432.png]]
	 - ![[Pasted image 20240804230436.png]]
	 - 实现原理
	 - ![[Pasted image 20240804230442.png]]
	 - 细节
	 - ![[Pasted image 20240804230448.png]]
	 - ![[Pasted image 20240804230452.png]]
- Session
	- 使用
	- ![[Pasted image 20240804230505.png]]
	- ![[Pasted image 20240804230507.png]]
	- 原理
	- ![[Pasted image 20240804230515.png]]
	- 细节
	- ![[Pasted image 20240804230525.png]]
	- ![[Pasted image 20240804230529.png]]
	- 登录页面
	- ![[Pasted image 20240804230540.png]]

---

## JSP

 - ![[Pasted image 20240804230556.png]]
 - 原理
 - ![[Pasted image 20240804230602.png]]
 - 脚本
 - ![[Pasted image 20240804230608.png]]
 - 内置对象
 - ![[Pasted image 20240804230624.png]]
 - ![[Pasted image 20240804230627.png]]
 - 注释
 - ![[Pasted image 20240804230634.png]]
 - 指令
 - ![[Pasted image 20240804230640.png]]
 - ![[Pasted image 20240804230642.png]]

---

## MVC

 - 在Spring中也有[MVC](obsidian://open?vault=Obsidian&file=SSM%2F08%20SpringMVC)
 - ![[Pasted image 20240804230659.png]]
 - 演变过程
 - ![[Pasted image 20240804230910.png]]
 - 结构
 - ![[Pasted image 20240804230921.png]]
 - 优点
 - ![[Pasted image 20240804230928.png]]
 - EL表达式
 - ![[Pasted image 20240804230935.png]]
 - ![[Pasted image 20240804230939.png]]
 - ![[Pasted image 20240804230941.png]]
 - ![[Pasted image 20240804230943.png]]
 - 隐式对象
 - ![[Pasted image 20240804230951.png]]
 - 三层架构
 - ![[Pasted image 20240804230957.png]]
 - ![[Pasted image 20240804231000.png]]

---

## JSTL

 - ![[Pasted image 20240804231013.png]]
 - 常用标签
 - ![[Pasted image 20240804231021.png]]
 - ![[Pasted image 20240804231024.png]]
 - ![[Pasted image 20240804231026.png]]
 - ![[Pasted image 20240804231029.png]]
 - ![[Pasted image 20240804231033.png]]
 - ![[Pasted image 20240804231036.png]]
 - ![[Pasted image 20240804231038.png]]
 - ![[Pasted image 20240804231043.png]]
 - ![[Pasted image 20240804231046.png]]

---

## 实例_用户信息

 - ![[Pasted image 20240804231105.png]]
 - 开发
	 - ![[Pasted image 20240804231115.png]]
	 - ![[Pasted image 20240804231117.png]]
	 - ![[Pasted image 20240804231121.png]]
	 - ![[Pasted image 20240804231126.png]]
- 增
	- ![[Pasted image 20240804231136.png]]
- 删
	- ![[Pasted image 20240804231144.png]]
	- ![[Pasted image 20240804231146.png]]
- 改
	- ![[Pasted image 20240804231154.png]]
- 分页查询
	- ![[Pasted image 20240804231202.png]]
	- ![[Pasted image 20240804231206.png]]
	- ![[Pasted image 20240804231212.png]]
	- ![[Pasted image 20240804231219.png]]

---

## Filter

 - MVC中的 [[08 SpringMVC#拦截器]]

 - ![[Pasted image 20240804231343.png]]
 - 使用
 - ![[Pasted image 20240804231350.png]]
 - ![[Pasted image 20240804231353.png]]
 - xml配置
 - ![[Pasted image 20240804231358.png]]
 - ![[Pasted image 20240804231401.png]]
 - 两个文件被同一个过滤器管理
 - ![[Pasted image 20240804231406.png]]
 - ![[Pasted image 20240804231409.png]]
 - ![[Pasted image 20240804231412.png]]
 - 执行流程
 - ![[Pasted image 20240804231418.png]]
 - 生命周期
 - ![[Pasted image 20240804231424.png]]
 - 资源访问
 - ![[Pasted image 20240804231431.png]]
 - ![[Pasted image 20240804231434.png]]
 - ![[Pasted image 20240804231437.png]]
 - ![[Pasted image 20240804231439.png]]
 - 过滤器链
 - ![[Pasted image 20240804231447.png]]
 - ![[Pasted image 20240804231451.png]]
 - 案例
	 - ![[Pasted image 20240804231459.png]]
	 - ![[Pasted image 20240804231501.png]]
	 - ![[Pasted image 20240804231504.png]]
	 - ![[Pasted image 20240804231507.png]]
	 - ![[Pasted image 20240804231511.png]]
- 增强对象
- ![[Pasted image 20240804231520.png]]
- ![[Pasted image 20240804231523.png]]
- ![[Pasted image 20240804231525.png]]
- ![[Pasted image 20240804231528.png]]


---

## Listener

 - ![[Pasted image 20240804231548.png]]
 - 对象
 - ![[Pasted image 20240804231553.png]]
 - 步骤
 - ![[Pasted image 20240804231559.png]]
 - ![[Pasted image 20240804231602.png]]
 - ![[Pasted image 20240804231604.png]]
 - ![[Pasted image 20240804231612.png]]