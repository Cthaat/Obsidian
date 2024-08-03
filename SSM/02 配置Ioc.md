---
tags: java,spring
---

---

## Maven导包

```xml
<dependency>  
    <groupId>org.springframework</groupId>  
    <artifactId>spring-context</artifactId>  
    <version>5.2.10.RELEASE</version>  
</dependency>
```

---

## 配置xml

```xml
<?xml version="1.0" encoding="UTF-8"?>  
<beans xmlns="http://www.springframework.org/schema/beans"  
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">  
    <!-- Spring 版本 5.2.10.RELEASE  -->    <!-- 配置bean -->  
    <bean id="userService" class="com.example.demo.service.UserService">  
</beans>
```

 - 配置属性
 - ![[Pasted image 20240706164549.png]]
 - ![[Pasted image 20240706164631.png]]
 - ![[Pasted image 20240706164637.png]]
 - ![[Pasted image 20240706164644.png]]

---

