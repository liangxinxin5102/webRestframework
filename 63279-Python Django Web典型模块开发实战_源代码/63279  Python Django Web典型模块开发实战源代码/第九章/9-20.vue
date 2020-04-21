<template>
  <div id="app">
	<!--……-->
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
//向后端发送数据请求
    getData(){
      axios({
        url:'http://127.0.0.1:8000/book/’
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
</style>
