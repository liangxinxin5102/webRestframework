<template>
  <div id="app">
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>
<script>
//引入axios模块
import axios from 'axios'
export default {
  name: 'App',
  data(){
    return{
      msg:''
    }
  },
  methods:{
//向后端项目请求数据方法
    getData(){
      axios({
        url:'api/book/'
      }).then(res=>{
        console.log(res)
      })
    }
  },
  mounted(){
    this.getData()
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
  margin-top: 60px;
}
</style>
