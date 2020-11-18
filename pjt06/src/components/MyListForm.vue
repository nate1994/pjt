<template>
  <div>
    <input type="text" v-model="movietitle" @keypress.enter="createList">
    <button class="ml-1" @click="createList"> + </button>
  </div>
</template>

<script>
export default {
  name : "MyListForm", //데이터를 입력하고 저장하는
  data(){
    return{
      movietitle :""
    }
  },
  methods:{
    createList(){
      const movie ={
        id : new Date().getMilliseconds(),
        movietitle : this.movietitle,
      }
    this.$store.dispatch('createList',movie)
    this.movietitle = ""
    }
  }

}
</script>

<style>

</style>