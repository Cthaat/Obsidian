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

---

## axios

 - 请求访问拦截
 - 响应访问拦截

``` javascript
import axios from 'axios'

import { useUserStore } from '@/stores/modules/user'

import { ElMessage } from 'element-plus/es/components'

import router from '@/router/index'

  

const baseURL = 'http://big-event-vue-api-t.itheima.net'

  

// 创建axios实例

const instance = axios.create({

  // TODO 基础地址，超时时间

  baseURL,

  timeout: 10000

})

  

// 请求拦截器

instance.interceptors.request.use(

  (config) => {

    // TODO 请求拦截器，携带 token 等信息

    const userStore = useUserStore()

    if (userStore.token) {

      config.headers.Authorization = userStore.token

    }

    return config

  },

  (err) => Promise.reject(err)

)

  

// 响应拦截器

instance.interceptors.response.use(

  (res) => {

    // TODO 摘取核心响应数据

    if (res.data.code === 0) {

      return res

    }

    // TODO 响应拦截器，处理响应数据，处理业务失败

    ElMessage.error(res.data.message || '请求失败')

    return Promise.reject(res.data)

  },

  (err) => {

    // TODO 错误处理401

    if (err.response.status === 401) {

      ElMessage.error('请先登录')

      router.push('/login')

      return Promise.reject(err)

    }

    // TODO 错误处理500

    ElMessage.error(err.response.data.message || '请求失败')

    return Promise.reject(err)

  }

)

  

export default instance

export { baseURL }
```

---

## 路由配置

 - 配置一级路由和二级路由
 - 访问网站的时候自动重定向

``` javascript
routes: [

    {

      path: '/login',

      component: () => import('@/views/login/loginPage.vue')

    },

    {

      path: '/',

      component: () => import('@/views/layout/layoutContainer.vue'),

      redirect: '/article/manage',

      children: [

        {

          path: 'article/manage',

          component: () => import('@/views/article/articleManage.vue')

        },

        {

          path: 'article/channel',

          component: () => import('@/views/article/articleChannel.vue')

        },

        {

          path: 'user/avatar',

          component: () => import('@/views/user/userAvatar.vue')

        },

        {

          path: 'user/profile',

          component: () => import('@/views/user/userProfile.vue')

        },

        {

          path: 'user/password',

          component: () => import('@/views/user/userPassword.vue')

        }

      ]

    }

  ]
```

---

## 表单校验

 - 表单需要绑定数据和校验规则
 - 表单元素需要绑定具体数据和对应规则
 - ![[Pasted image 20240722184312.png]]

``` javascript
const formModel = ref({

  username: '',

  password: '',

  repassword: ''

})

const rules = ref({

  username: [

    {

      required: true,

      message: '请输入用户名',

      trigger: 'blur'

    },

    {

      min: 1,

      max: 10,

      message: '用户名长度在 1 到 10 个字符',

      trigger: 'blur'

    }

  ],

  password: [

    {

      required: true,

      message: '请输入密码',

      trigger: 'blur'

    },

    {

      patton: /^\S{6,15}$/,

      message: '密码长度在 6 到 15 个非空字符',

      trigger: 'blur'

    }

  ],

  repassword: [

    {

      required: true,

      message: '请再次输入密码',

      trigger: 'blur'

    },

    {

      patton: /^\S{6,15}$/,

      message: '密码长度在 6 到 15 个非空字符',

      trigger: 'blur'

    },

    {

      validator: (rule, value, callback) => {

        if (value !== formModel.value.password) {

          callback(new Error('两次输入的密码不一致!'))

        } else {

          callback()

        }

      },

      trigger: 'blur'

    }

  ]

})
```

---

## api 封装

 - 对后端提供的api进行使用
 - 使用[[#axios]]写好的拦截器进行使用

``` javascript
import request from '../utils/request'

  

export const userRegisterService = ({

  username,

  password,

  repassword

}) => {

  return request.post('/api/reg', { username, password, repassword })

}

  

export const userLoginService = ({ username, password }) => {

  return request.post('/api/login', { username, password })

}
```

