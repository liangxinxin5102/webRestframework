<template>
  <div id="app">
      <div class="userinfo">
        用户名：{{username}}
      </div>
      <div class="login" v-if="flag">
        <input type="text" v-model="username">
        <input type="text" v-model="pwd">
        <button>登录</button>
      </div>
      <div class="article">
        <div class="title">文章标题</div>
        <div class="content">文章内容</div>
      </div>
      <div class="makecomment">
        <div>评论内容<input type="text" v-model="comment"></div>
        <button>提交评论</button>
      </div>
      <div class="commentlist">
        <div class="commentcontent">评论内容</div>
      </div>
      <div class="makearticle">
        <div class="title">文章标题 <input type="text" v-model="title"> </div>
        <div class="content">文章内容 <input type="text" v-model="content"> </div>
        <button>提交文章</button>
      </div>
  </div>
</template>
<script>
export default {
  name: 'app',
  data () {
    return {
      username: 'root',
      pwd:'',
      flag:true,
      article:[],
      title:'',
      comment:''
    }
  }
}
</script>

<style>
.userinfo{
  width: 300px;
  margin: 0 auto;
}
.login{
  width: 300px;
  margin: 0 auto;
}
.login input{
  width: 200px;
  margin: 0 auto;
}
.article{
  width: 300px;
  margin: 0 auto;
}
.makecomment{
  width: 300px;
  margin: 0 auto;
}
.commentlist{
  width: 300px;
  margin: 0 auto;
}
.makearticle{
  width: 300px;
  margin: 0 auto;
}
</style>
