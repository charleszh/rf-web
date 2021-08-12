// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import store from './store'
import App from './App'
import router from './router'
import { getRefreshToken } from '../lib/format'
import ElementUI from 'element-ui'
import { Message } from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// 设置反向代理，前端请求默认发送到 http://localhost:8443/api
var axios = require('axios')
axios.defaults.baseURL = 'http://localhost:8000/api'
// axios.defaults.withCredentials = false
// 全局注册，之后可在其他组件中通过 this.$axios 发送数据
Vue.prototype.$axios = axios
Vue.config.productionTip = false

// 添加请求拦截器，在请求头中加token
axios.interceptors.request.use(
  config => {
    let token = store.state.token
    if (token) {
      config.headers.Authorization = 'JWT ' + token
    }
    return config
  },
  error => {
    return Promise.reject(error)
  })
// http response 拦截器
axios.interceptors.response.use(
  response => {
    // let token = store.state.token // localStorage.getItem('Authorization')
    console.log('in resp: ', response.data.token)
    if (!response.data.token) { // 有没有token
      let refreshToken = store.state.refreshToken
      getRefreshToken(refreshToken).then(res => {
        // store.state.token = res.data.token
        // store.state.refreshToken = res.data.token
        store.commit('setToken', res.token)
        store.commit('setRefreshToken', res.token)
      })
    } else window.isReresh = false
    return response
  }, // 请求成功的时候返回的data,
  error => {
    try {
      if (error.response) {
        // endLoading()
        switch (error.response.status) {
          case 401:// token过期，清除它,清除token信息并跳转到登录页面
            // store.commit('DelToken')
            console.log('401 fired')
            Message({
              showClose: true,
              message: '请重新登录！',
              type: 'error',
              duration: 1000 })
            router.replace({
              path: '/login',
              query: {
                redirect: router.currentRoute.fullPath// 登录之后跳转到对应页面
              }
            })
            return
          case 403:// 权限
            store.commit('DelToken')
            router.replace({
              path: '/login',
              query: {
                redirect: router.currentRoute.fullPath// 登录之后跳转到对应页面
              }
            })
            return
        }
      }
      return Promise.reject(error.response.data)
    } catch (e) {
    }
  })

Vue.use(ElementUI)
router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      next()
    } else {
      next({
        path: 'login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next()
  }
}
)
/*

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
// axios拦截器，目的是为了在请求头上带上token
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('Authorization')) {
      // token字段是要和后端协商好的
      config.headers.common['token'] = localStorage.getItem('Authorization')
      // debugger
    }
    return config
  },
  error => {
    return Promise.reject(error)
  })
*/

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
