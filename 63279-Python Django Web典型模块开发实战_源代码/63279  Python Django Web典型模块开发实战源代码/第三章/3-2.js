<script>
export default {
  name: 'app',
  data () {
    return {
      one:['一级类目','一级类目','一级类目','一级类目','一级类目'],
      two:['二级类目1','二级类目2','二级类目3','二级类目4','二级类目5'],
      three:[],
      four:['四级类目','四级类目','四级类目','四级类目','四级类目'],
      flag:false
    }
  },
  methods: {
    open(index){
      var index=index+1;
      var i=index+"";
      this.three=['三级目录'+i,'三级目录'+i,'三级目录'+i,'三级目录'+i,'三级目录'+i]
      this.flag=true
    },
    close(){
      this.flag=false
    }
  },
}
</script>
