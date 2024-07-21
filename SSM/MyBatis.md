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
 - 注意Java中int类型默认不是null而是0
```xml
<select id="select" resultType="org.example.user.user">  
    select *  
    from test    where    <choose>  
        <when test="name != null and name != ''">  
            name = #{name}  
        </when>  
        <when test="id != 0">  
            id = #{id}  
        </when>  
        <otherwise>  
            1 = 1  
        </otherwise>  
    </choose>  
    ;  
</select>
```

---

## 添加

 - 在xml中写语句
 - 直接执行，并且执行后要进行提交
 - 默认自动提交是关闭的
 - 创建sqlSession的时候可以传入true参数打开自动提交
<br/>
 - 主键返回
 - 有的主键是自动生成的
 - 需要获取自动生成的主键的时候

```xml
<insert id="add" useGeneratedKeys="true" keyProperty="id">  
    insert into test (workno, name)  
    values (#{workno}, #{name});</insert>
```