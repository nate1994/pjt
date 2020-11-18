<template>
  <div>
    <h2>RANDOM</h2>
    <button @click="randomChoice">돌려라돌려</button>
    <br>
    <span>{{movieTitle}}</span>

  </div>
</template>

<script>
import _ from "lodash"

export default {
  name: 'Random',
  data (){
    return {
      movieTitleList : ['해리포터', '어벤져스1','어바웃타임','노트북', '테넷'],
      movieTitle : ""
    }
  },
  methods :{
    randomChoice(){
      const idx = _.random(this.movieTitleList.length-1)
      this.movieTitle = this.movieTitleList[idx]
    }
  }
}
</script>
