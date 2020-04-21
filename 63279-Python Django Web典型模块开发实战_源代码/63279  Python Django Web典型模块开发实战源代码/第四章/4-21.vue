goRegister(){
      //提交完整的注册信息
      var api='http://127.0.0.1:8000/register/';
      Axios.get(api,{
          params:{
            phone:this.phone,
            username:this.username,
            pwd:this.pwd,
            code:this.code,
		   email:this.email
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
