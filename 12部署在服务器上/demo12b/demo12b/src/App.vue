<template>
  <div id="app">
    <div class="t">{{title}}</div>
    <div v-for="(item,index) in twdata" :key="index">
      <div>{{item.title}}</div>
      <img :src="item.image" alt="">
    </div>
  </div>
</template>

<script>
  import Axios from 'axios';
export default {
  name: 'App',
    data(){
      return{
          title:'首页',
          twdata:[]
      }
    },
    methods: {
        GetData(){
            var that=this
            const host='http://127.0.0.1:8000'
            var api=host+'/getdata/';
            Axios.get(api)
                .then(function (response) {
                    // console.log(response.data)
                    for(var i=0;i<response.data.length;i++){
                        response.data[i].image=host+response.data[i].image
                    }
                    // console.log(response.data)
                    that.twdata=response.data
                })
                .catch(function (error) {
                    console.log(error);
                });
        }
    },
    mounted() {
        this.GetData()
    }
}
</script>

<style>
  .t{
    width: 100px;
    height: 100px;
    background-color: brown;
    line-height: 100px;
    text-align: center;
  }
  img{
    width: 200px;
    height: 200px;
  }
</style>
