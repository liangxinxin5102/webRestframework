<template>
  <div id="app">
    <h1>{{title}}</h1>
    <div class="registerwindow">
      <div class="title">用户注册</div>
      <div class="item">
        <div class="text">用户名:</div>
        <input type="text">
      </div>
      <div class="item">
        <div class="text">密码:</div>
        <input type="text">
      </div>
      <div class="item">
        <div class="text">手机号:</div>
        <input type="text">
        <button>获取验证码</button>
      </div>
      <div class="item">
        <div class="text">验证码:</div>
        <input type="text">
        <button>确认注册</button>
      </div>
    </div>
    
  </div>
</template>
<script>
export default {
  name: 'app',
  data () {
    return {
      title: '首页',
      codebtn:'获取验证码'
    }
  }
}
</script>
<style>
*{
  margin:0;
  padding: 0;
  box-sizing: border-box;
}
.registerwindow{
  margin: 0 auto;
  width: 350px;
  height: 200px;
  background: rgba(5, 55, 148, 0.5);
}
.title{
  margin: 0 auto;
  font-size: 30px;
  text-align: center
}
.item{
  margin-top:10px; 
  display: flex;
  flex-direction: row;
}
.text{
  text-align: center;
  width: 80px;
}
input{
  width: 140px;
}
button{
  width: 80px;
  margin-left: 5px;
}
</style>
