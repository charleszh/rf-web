<template>
  <div id="app">
    <!--keep-alive :exclude="excludeComponents"-->
      <router-view></router-view>
    <!--/keep-alive-->
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'
export default {
  name: 'App',
  computed: mapState({
    'count': state => state.count,
    excludeComponents () {
      var that = this
      console.log(that.count)
      return []
    }
  }),
  methods: {
    ...mapActions([
      'actionAdd',
      'actionReduce'
    ])
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 10px;
}
</style>
