---
tags: vue,nuxt
---

---

## 问题

 - 提示无法连接

---

## 解决

 - 设置证书
 - There will be an issue with SSL certificate verification in localhost that's why this error occurred. to stop this add `NODE_TLS_REJECT_UNAUTHORIZED=0` in your root `.env` file. using this way, the error will be fixed and still you can use the SSR feature.  
 - 本地主机中的 SSL 证书验证存在问题，这就是发生此错误的原因。要停止此操作，请在根 `.env` 文件中添加 `NODE_TLS_REJECT_UNAUTHORIZED=0` 。使用这种方式，错误将被修复，并且您仍然可以使用 SSR 功能。
