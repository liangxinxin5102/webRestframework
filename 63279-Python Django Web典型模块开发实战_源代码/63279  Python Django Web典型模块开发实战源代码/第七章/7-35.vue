<template>
  <div id="app">
      <div class="userinfo">
        用户名：{{username}}
      </div>
      <div class="login" v-if="flag">
        <input type="text" v-model.lazy="username">
        <button @click="Login()">登录</button>
      </div>
      <div class="article" v-for="(item,index) in article" :key=index>
        <div class="title">{{item.title}}</div>
        <div class="content">{{item.content}}</div>
      </div>
      <div class="commentlist" v-for="item in comment" :key=item.content>
        <div class="commentcontent">{{item.content}}</div>
      </div>
      <div class="makecomment">
        评论内容:<input type="text" v-model="pushcommet">
        <button @click="PushComment()">提交评论</button>
      </div>
      <div class="makearticle">
        <div class="title">文章标题 <input type="text" v-model="title"> </div>
        <div class="content">文章内容 <input type="text" v-model="content"> </div>
        <button @click="PushArticle()">提交文章</button>
      </div>   
  </div>
</template>
<script>
import Axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      username: '',
      id:'',
      flag:true,
      article:[],
      title:'',
      content:'',
      comment:[],
      pushcommet:''
    }
  },
  methods:{
//登录方法
    Login(){
      var api='http://127.0.0.1:8000/login/?username='+this.username
       Axios.get(api)
      .then((response)=>{
        // console.log(response.data.username);
        this.username=response.data.username
        this.id=response.data.id
        if(this.id){
          this.flag=false
        }       
        })
      .catch((error)=>{
        console.log(error)
        }
      )
},
//获取文章列表的方法
    GetArticle(){
      var api='http://127.0.0.1:8000/getarticle/'
      Axios.get(api)
      .then((response)=>{
        console.log(response.data);
        this.article=response.data
        })
      .catch((error)=>{
        console.log(error)
        }
      )
},
//获取评论的方法
    GetComment(){
      var api='http://127.0.0.1:8000/getcomment/'
      Axios.get(api)
      .then((response)=>{
        console.log(response.data);
        this.comment=response.data
        })
      .catch((error)=>{
        console.log(error)
        }
      )
},
//发表文章的方法
    PushArticle(){
      var api='http://127.0.0.1:8000/pusharticle/'
      var params = new URLSearchParams();
      params.append("title",this.title);
      params.append("content",this.content);
      params.append("id",this.id);
      console.log(params)
      Axios.post(api,params)
      .then((response)=>{
        console.log(3333,response);
        if(response.data!=200){
          alert('存在违禁词')
        }
        this.GetArticle()
        })
      .catch((error)=>{
        console.log(error)
        }
      )
    },
//发表评论的方法
    PushComment(){
      var api='http://127.0.0.1:8000/pushcomment/'
      let data = {"title":this.title,"comment":this.pushcommet,"id":this.id};
      var params = new URLSearchParams();
      params.append("comment",this.pushcommet);
      params.append("id",this.id);
      console.log(params)
      Axios.post(api,params)
      .then((response)=>{
        console.log(response);
        this.GetComment()
        })
      .catch((error)=>{
        console.log(error)
        }
      )
    }
  },
  mounted(){
    this.GetArticle();
    this.GetComment()
  }
}
</script>
<style>
*{
  box-sizing: border-box;
}
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
  margin-top: 20px;
  margin-bottom: 10px;
  border: 2px solid;
  padding: 5px;
}
.article .title{
  border-bottom: 1px solid;
}
.makecomment{
  width: 300px;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 10px;
}
.makecomment input{
  width: 150px;
}
.commentlist{
  width: 300px;
  margin: 0 auto;
  margin-top: 20px;
  margin-bottom: 10px;
  border-bottom: 1px solid;
  padding: 5px;
}
.makearticle{
  width: 300px;
  margin: 0 auto;
}
</style>
