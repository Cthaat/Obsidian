---
tags: spring, java
---

---

## 整合流程

 - ![[Pasted image 20240803221806.png]]
<br />
 - 整合mybatis
 - ![[Pasted image 20240804135405.png]]
 - ![[Pasted image 20240804135425.png]]
 - ![[Pasted image 20240804135431.png]]
 - ![[Pasted image 20240804135439.png]]
 - ![[Pasted image 20240804135449.png]]
 - ![[Pasted image 20240804135457.png]]
 - 注意如果使用xml配置
```java
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.mapper.MapperScannerConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

@Configuration
public class MyBatisConfig {

    @Bean
    public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception {
        SqlSessionFactoryBean sqlSessionFactoryBean = new SqlSessionFactoryBean();
        sqlSessionFactoryBean.setDataSource(dataSource);
        sqlSessionFactoryBean.setTypeAliasesPackage("com.example.domain");

        // 设置Mapper XML文件路径
        Resource[] resources = new PathMatchingResourcePatternResolver().getResources("classpath*:com/example/dao/*.xml");
        sqlSessionFactoryBean.setMapperLocations(resources);

        return sqlSessionFactoryBean.getObject();
    }

    @Bean
    public MapperScannerConfigurer mapperScannerConfigurer() {
        MapperScannerConfigurer mapperScannerConfigurer = new MapperScannerConfigurer();
        mapperScannerConfigurer.setBasePackage("com.example.dao");
        return mapperScannerConfigurer;
    }
}

```
 - 要配置xml的路径
 - 事务处理
 - ![[Pasted image 20240804135515.png]]
<br />
 - 整合MVC
 - ![[Pasted image 20240804135547.png]]
 - ![[Pasted image 20240804135558.png]]
 - ![[Pasted image 20240804135604.png]]
 - ![[Pasted image 20240804135624.png]]
 - 放行处理
 - ![[Pasted image 20240804161126.png]]
 - 新建一个类，放行处理
 - ![[Pasted image 20240804161156.png]]
 - 同时在MVC中处理
 - ![[Pasted image 20240804161213.png]]
---

## 异常处理

 - 原因
 - ![[Pasted image 20240804145829.png]]
 - 处理器
 - ![[Pasted image 20240804150514.png]]
 - ![[Pasted image 20240804151109.png]]
 - 异常处理方案
 - ![[Pasted image 20240804151242.png]]
<br />
 - ![[Pasted image 20240804152945.png]]
 - ![[Pasted image 20240804152952.png]]
 - ![[Pasted image 20240804152958.png]]
 - ![[Pasted image 20240804153006.png]]
 - ![[Pasted image 20240804153018.png]]
 - ![[Pasted image 20240804153027.png]]