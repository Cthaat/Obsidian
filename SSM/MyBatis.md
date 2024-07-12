---
tags: Spring,Sql
---

---

## 使用代理模式

 - ![[Pasted image 20240712160117.png]]
 - 在同一个包下创建这两个，一个Java类，一个xml配置
 - ![[Pasted image 20240712160200.png]]
 - 注意创建的时候用斜杠创建
 - ![[Pasted image 20240712160221.png]]
 - 让namespace和类名一样
 - ![[Pasted image 20240712160237.png]]
 - 在类中创建方法

---

## 核心配置文件


 - environments
	 - default可以切换不同的环境
	 - ![[Pasted image 20240712162856.png]]
 - typeAliases
	 - 可以设置类型别名和包名称
	 - ![[Pasted image 20240712163403.png]]

---

## 驼峰命名法和下划线命名转换

 - Java为驼峰命名法
 - sql中为下划线名法
 - ![[Pasted image 20240712165403.png]]

---

## 设置参数

![[Pasted image 20240712214218.png]]

---

## 动态条件查询

 - if语句
```xml
select *  
from test  
<where>  
    <if test="id!= null">  
        and id = #{id}  
    </if>  
    <if test="name!= null">  
        and name = #{name}  
    </if>  
</where>
```

 - choose
```xml

```