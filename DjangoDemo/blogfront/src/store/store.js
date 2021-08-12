import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
let store = new Vuex.Store({
  state: {
    excludeComponents: [],
    count: 1
  },
  actions: {
    actionAdd (context, n) {
      /* return new Promise((resolve, reject) => {
        setTimeout(() => {
          context.commit('add', n)
          resolve()
        })
      }) */
      setTimeout(() => {
        context.commit('add', n)
      }, 2000)
      // context.commit('add', n)
      console.log('First execution')
    },
    actionReduce (context, n) {
      // return new Promise((resolve, reject) => {
      //   setTimeout(() => {
      //     context.commit('reduce', n)
      //     resolve()
      //   })
      // })
      context.commit('reduce', n)
    }
  },
  mutations: {
    add (state, n) {
      state.count += n
    },
    reduce (state, n) {
      state.count -= n
    }
  }
})
export default store
