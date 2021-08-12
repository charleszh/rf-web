import Vue from 'vue'
import Router from 'vue-router'
// import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/login/',
      name: 'Login',
      component: () => import('../components/Login')
    },
    {
      path: '/register/',
      name: 'Register',
      component: () => import('../components/Register')
    },
    {
      path: '/',
      name: 'AtmsIndex',
      component: () => import('../components/AtmsIndex'),
      // component: () => import('../components/ShowLog'),
      meta: {
        requireAuth: true
      },
      children: [
        {
          path: '/show_testcases/',
          name: 'TestCaseList',
          component: () => import('../components/TestCaseList'),
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/index/',
          name: 'Home',
          component: () => import('../components/Home'),
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/execute_testcase/',
          name: 'ExecutePage',
          component: () => import('../components/ExecutePage'),
          meta: {
            requireAuth: true
          }
        },
        {
          path: '/show_pathtree',
          name: 'ShowPathTree',
          component: () => import('../components/ShowPathTree'),
          meta: {
            keepAlive: true,
            requireAuth: true
          }
        }
      ]
    }
  ]
})
