'/api': { //替换代理地址名称
        target: 'http://127.0.0.1:8000/', //代理地址
       changeOrigin: true, //可否跨域
       pathRewrite: {
       '^/api': '' //重写接口，去掉/api
        }
      }
