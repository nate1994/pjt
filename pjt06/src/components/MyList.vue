<template>
  <div>
    <div v-for="movie in movieList" :key="movie.id">
      <p class="title">{{movie.movietitle}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name : "MyList", // 출력하는...
  computed :{
    movieList(){
      return this.$store.state.movieList
    }
  }
}
</script>

<style>

</style>