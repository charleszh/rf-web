import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: {
      username: window.localStorage.getItem('user' || '[]') == null ? '' : JSON.parse(window.localStorage.getItem('user' || '[]')).username
    },
    token: '',
    refreshToken: ''
  },
  mutations: {
    login (state, user) {
      state.user = user
      window.localStorage.setItem('user', JSON.stringify(user))
    },
    setToken (state, token) {
      state.token = token
      localStorage.token = token
    },
    setRefreshToken (state, token) {
      state.refreshToken = token
      localStorage.refreshToken = token
    },
    logout (state) {
      state.user = []
      window.localStorage.clear()
      /*      window.localStorage.removeItem('user')
      window.localStorage.removeItem('token')
      window.localStorage.removeItem('refreshToken') */
    }
  },
  getters: {
    getToken (state) {
      if (!state.token) {
        state.token = localStorage.getItem('token')
      }
      return state.token
    },
    getRefreshToken (state) {
      if (!state.refreshToken) {
        state.refreshToken = localStorage.getItem('refreshToken')
      }
      return state.refreshToken
    }
  }
})
