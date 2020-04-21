<template>
  <div id="app">
    <div class="search">
      关键词：<input type="text"><button>搜索</button>
    </div>
    <div class="list">
      <div class="article">
        <div class="title">标题</div>
        <div class="content">内容内容内容内容内容内容内容内容内容</div>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      keyword: '',
      article:[]
    }
  },
  methods:{ 
  }
}
</script>
<style>
</style>
