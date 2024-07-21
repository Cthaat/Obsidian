---
tags: vue
---

---

## pnpm

 - 包管理器
 - 创建项目
 - ![[Pasted image 20240721221256.png]]

---

## Eslint

 - 代码风格检查
 - 配置代码风格
<br/>
 - 安装插件
 - ![[Pasted image 20240721221616.png]]

``` javascript
/* eslint-env node */

require('@rushstack/eslint-patch/modern-module-resolution')

  

module.exports = {

  root: true,

  extends: [

    'plugin:vue/vue3-essential',

    'eslint:recommended',

    '@vue/eslint-config-prettier/skip-formatting'

  ],

  parserOptions: {

    ecmaVersion: 'latest'

  },

  rules: {

    'prettier/prettier': [

      'warn',

      {

        singleQuote: true,

        semi: false,

        printWidth: 100,

        trailingComma: 'none',

        endOfLine: 'auto',

        tabWidth: 2

      }

    ],

    'vue/multi-word-component-names': [

      'warn',

      {

        ignores: ['index']

      }

    ],

    'vue/no-setup-props-destructure': ['off'],

    'no-undef': 'error'

  }

}
```

---

## prettier

 - 将代码风格化
 - Esline是检查代码
 - 这个是更改代码
 - 将代码自动格式化
<br/>
```javascript
{

  "$schema": "https://json.schemastore.org/prettierrc",

  "semi": false,

  "tabWidth": 4,

  "singleQuote": true,

  "printWidth": 100,

  "trailingComma": "none"

}
```

---

## husky

 - 在代码提交前对代码进行检查
 - 是git的hook
 - 对代码进行错误检查，如果有错就无法提交
<br/>
 - 安装
 - ![[Pasted image 20240721221854.png]]
 - 将文件修改为对应的包管理器
 - ![[Pasted image 20240721221906.png]]
<br/>
 - 使用line-staged
 - 这个插件是只是检查自己最新写的代码
 - ![[Pasted image 20240721222029.png]]

---

## Element-plus

 - vue的组件库
 - [官网](https://element-plus.org/zh-CN/guide/design.html)有导入方式

---

## pinia

 - 全局状态管理库
 - 管理用户个人信息等
<br/>
```javascript
import { defineStore } from 'pinia'

import { ref } from 'vue'

  

export const useUserStore = defineStore(

  'big-user',

  () => {

    const token = ref('')

    const setToken = (newToken) => {

      token.value = newToken

    }

    const removeToken = () => {

      token.value = ''

    }

    return {

      token,

      setToken,

      removeToken

    }

  },

  {

    persist: true

  }

)
```

  - pinia持久化插件
  - [官方](https://prazdevs.github.io/pinia-plugin-persistedstate/zh/)有导入方式
<br/>
 - pinia单独管理
```javascript
import { createPinia } from 'pinia'

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

  

const pinia = createPinia()

  

pinia.use(piniaPluginPersistedstate)

  

export default pinia
```

 - 将pinia导出后在main.js导入
 - 将pinia挂载