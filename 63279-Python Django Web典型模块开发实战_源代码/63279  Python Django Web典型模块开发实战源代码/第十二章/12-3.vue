<template>
  <div id="app">
    <div class="t">{{title}}</div>
  </div>
</template>
<script>
import Axios from 'axios';
export default {
  name: 'App',
    data () {
    return {
      title:'Ê×Ò³'
    }
  },
  methods: {
    GetData(){
      const host='http://127.0.0.1:8000'
      var api=host+'/getgoodlist/';
      Axios.get(api)
      .then(function (response) {
          console.log(response)   
      })
      .catch(function (error) {
      console.log(error);
      });
    }
  },
  mounted() {
    // this.GetData()
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
</style>
