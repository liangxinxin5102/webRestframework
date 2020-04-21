<template>
  <div id="app">
    <div class="search">
      关键词：<input type="text" v-model="keyword"><button @click="GetList()">搜索</button>
    </div>
    <div class="list">
      <div class="article" v-for="(item,index) in article" :key=index>
        <div class="title">{{item.title}}</div>
        <div class="content">{{item.content}}</div>
      </div>
      
    </div>
  </div>
</template>
<script>
//引入axios模块
import Axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      keyword: '',
      article:[]
    }
  },
  methods:{
//向后端提交关键词
    GetList(){
      var api='http://127.0.0.1:8000/getlist/?keyword='+this.keyword
      console.log(api)
      Axios.get(api)
      .then((response)=>{
        console.log(response);
        this.article=response.data
        })
      .catch((error)=>{
        console.log(error)
        }
      )
    }
  }
}
</script>
<style>
*{
  box-sizing: border-box;
}
.search{
  margin:0 auto;
  margin-top: 100px;
  width: 300px;
}
.article{
  width: 300px;
  margin:0 auto;
  margin-top: 20px;
  border: 2px solid;
  padding: 5px;
}
.title{
  border-bottom: 2px dashed royalblue;
}
</style>
