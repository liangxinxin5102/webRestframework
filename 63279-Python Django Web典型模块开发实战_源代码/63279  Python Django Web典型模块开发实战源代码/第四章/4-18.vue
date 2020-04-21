<script>
import Axios from 'axios';
export default {
//......
methods: {
    getCode(){
      //用来向后台发送请求获取验证码
      var api='http://127.0.0.1:8000/sendcode/';
      Axios.get(api,{
          params:{
            phone:this.phone
          }
        }  
      )
      .then((Response)=>{
        console.log(Response.data)
        // 根据返回的信息，做出响应的提示
      })
      .catch((error)=>{
        console.log(error)
      })
},
//......
