<template>
  <div id="app">
      <!--…… -->
    <v-active :email='email'></v-active>
  </div>
</template>
<script>
import Axios from 'axios';
import Active from './components/Active.vue';
export default {
  name: 'app',
  data () {
    return {
      title: '首页',
      disabled:false,
      time:0,
      codebtn:'获取验证码',
      phone:'',
      username:'',
      pwd:'',
      code:'',
      email:''
    }
  },
  components:{
    'v-active':Active
  },
//......
}
</script>
