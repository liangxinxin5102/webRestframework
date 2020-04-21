<script>
import Axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      type:[],
      one:[],
      two:[],
      flag:false,
      three1:[],
      four1:[]
    }
  },
  methods: {
    getData(){
      const api='http://127.0.0.1:8000/api/type/';
      var _this=this
      
      Axios.get(api)
      .then(function (response) {
        _this.type=response.data;
        for(var i=0;i<_this.type.length;i++){
          if(_this.type[i].category_type===1){
            _this.one.push(_this.type[i])
          } 
        }
        for(var j=0;j<_this.type.length;j++){
          if(_this.type[j].category_type===2){
            _this.two.push(_this.type[j])
          } 
        }
      })
      .catch(function (error) {
      console.log(error);
      });
      
    },
    open(index){
      this.three1=[]
      this.four1=[]
      var parent=this.two[index].id
      for(var i=0;i<this.type.length;i++){
        if(this.type[i].parent_category===parent){
          this.three1.push(this.type[i].name)
        }
        if(this.type[i].category_type===4){
          this.four1.push(this.type[i].name)
        }
      }
      this.flag=true
    },
    close(){
      this.flag=false
    }
  },
  mounted() {
    this.getData()
  }
}
</script>
