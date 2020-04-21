<script>
import Axios from 'axios';
export default {
  name: 'app',
  data () {
    return {
      one:[],
      two:[],
      three:[],
      four:[],
      flag:false,
      three1:[],
      four1:[]
    }
  },
  methods: {
    getData(){
      const api='http://127.0.0.1:8000/';
      var api1=api+'api/type1/';
      var api2=api+'api/type2/';
      var api3=api+'api/type3/';
      var api4=api+'api/type4/';
      var type1=[];
      var type2=[];
      var type3=[];
      var type4=[];
      Axios.get(api1)
      .then(function (response) {
      // console.log(response);
      for(var i=0;i<response.data.length;i++){
        // console.log(response.data[i])
        type1.push(response.data[i])
      }
      // console.log(type1)
      })
      .catch(function (error) {
      console.log(error);
      });
      this.one=type1;
      Axios.get(api2)
      .then(function (response) {
      // console.log(response);
      for(var i=0;i<response.data.length;i++){
        // console.log(response.data[i])
        type2.push(response.data[i])
      }
      // console.log(type2)
      })
      .catch(function (error) {
      console.log(error);
      });
      this.two=type2;
      Axios.get(api3)
      .then(function (response) {
      // console.log(response);
      for(var i=0;i<response.data.length;i++){
        // console.log(response.data[i])
        type3.push(response.data[i])
      }
      // console.log(type3)
      })
      .catch(function (error) {
      console.log(error);
      });
      this.three=type3;
      Axios.get(api4)
      .then(function (response) {
      // console.log(response);
      for(var i=0;i<response.data.length;i++){
        // console.log(response.data[i])
        type4.push(response.data[i])
      }
      // console.log(type4)
      })
      .catch(function (error) {
      console.log(error);
      });
      this.four=type4;
      // console.log(this.one)
      // console.log(this.two)
      // console.log(this.three)
      // console.log(this.four)
},
    open(index){
      // console.log(this.two[index].id)
      var temp=[]
      for(var i=0;i<this.three.length;i++){
        if(this.three[i].parent===index){
          temp.push(this.three[i].name)
        }
      }
      console.log(temp)
      this.three1=temp;
      var temp4=[]
      for(var j=0;j<this.four.length;j++){
        temp4.push(this.four[j].name)
      }
      this.four1=temp4
      this.flag=true
    },
    close(){
      this.flag=false
    }
  },
  mounted() {
    this.getData()
  },
}
</script>
