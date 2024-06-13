---
tags: Maven , IDEA
---

## 仓库

### 本地仓库
	- 优先从本地仓库查找jar包
	- 如果本地仓库没有则会从中央仓库查找
	- 如果架设私服，则会优先从私服中获取jar包

![[Pasted image 20240612203323.png]]

- 配置本地仓库

- - 打开D:\apache-maven-3.9.6\conf\setting
-  - 配置本地仓库目录
-  - ![[Pasted image 20240612203748.png]]
---
### 私服
   - 在D:\apache-maven-3.9.6\conf\setting中配置
-  ![[Pasted image 20240612203920.png]]
-  写入阿里云镜像
-  ![[Pasted image 20240612203936.png]]

---
### 中央仓库
    来自maven团队创建的仓库

---
## 项目

- 项目根目录
```
   .
   |----src  
   |     |----main  
   |     |         |----java ——存放项目的.java文件  
   |     |         |----resources ——存放项目资源文件，如spring, hibernate配置文件  
   |     |----test  
   |     |         |----java ——存放所有测试.java文件，如JUnit测试类  
   |     |         |----resources ——存放项目资源文件，如spring, hibernate配置文件  
   |----target ——项目输出位置

   |----pom.xml ----用于标识该项目是一个Maven项目
```

---
## 常用命令

- compile 编译文件为字节码文件
- clear 清理编译文件
- package 会打包称为war包，在taragt目录下，再打包前会先进行一次编译
- 编译打包顺序，先编译再打包，可以通过[[#生命周期]]了解更多
- install 将对应项目安装到[[#本地仓库]]

---
## IDEA中的Maven
- 因为IDEA中Maven是默认自带的Maven3
 默认仓库路径在C盘
 - 更改Maven设置
 ![[Pasted image 20240612211543.png]]
 在此处更改新建项目时候的默认设置就可以


---
## 生命周期

- Clean Lifecycle 构建前的清理
- Default Lifecycle 构建核心，编译，测试，打包
- Site Lifecycle 生成项目报告，站点

![[Pasted image 20240612214635.png]]

---

## 坐标

 - 被Maven管理的资源的唯一标识
 - groupld：组织名称
 - atifactld：模块名称
 - version：版本号
 - ![[Pasted image 20240612215433.png]]
 - 通过坐标可以确定唯一的一个jar包

---

## 编译插件

- alt+ins 插入插件模板
- ![[Pasted image 20240612224622.png]]
- 配置参数 jdk版本
- ![[Pasted image 20240612224707.png]]

---

## 打包web项目

- 创建webapp文件，注意必须在main文件夹下
- ![[Pasted image 20240613120325.png]]
- 补全WEB_INF和web.xml
- ![[Pasted image 20240613120357.png]]
- 在设置中的模板寻找web.xml 的模板
- 下载Tomcat7并配置
- ![[Pasted image 20240613123515.png]]
- 配置项目，运行，这样可以进行断点调试
- ![[Pasted image 20240613123455.png]]
- 

---

## 依赖

- 配置maven中的依赖项
- ![[Pasted image 20240613124332.png]]
---
## 依赖范围

- scope 就是依赖范围
	- compile **编译** **测试** **运行**都有效
	- test 只对**测试**环境有效
		- 在**测试**代码中可以使用
		- 用于**测试**环境
		- 打包后在包中不存在
		- 用于测试代码使用的依赖
	- provided 对**编译** **测试** 有效
		- servlet-api,因为Tomcat容器内部自带jar包，导入的时候又导入了jar包，运行的时候会发生冲突
	- runtime 对**测试** **运行**有效
		- JDBC驱动包
	- system 对**编译** **测试** 有效
		- 不常用，用于本地仓库之外的依赖
		- 需要指定目录