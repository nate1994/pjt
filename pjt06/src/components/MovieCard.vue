<template>
  <!-- <div>
    <img :src="movie.poster_path" alt="">
    <p>{{ movie.title }}</p>
    <p>{{ movie.overview }}</p>
    <br>
  </div> -->
  <div>
    <div class="container">
      <div class="row row-cols-1 row-cols-md-3">
        <div 
          v-for="movie in movieList"
          :key="movie.id"
          class="col mb-4"
        >
          <div class="card" style="width: 22rem;">
            <img :src="movie.poster_path" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">{{ movie.title }}</h5>
              <p class="card-text text-style">{{ movie.overview }}</p>
            </div>
          </div>  
        </div>
      </div>

      </div>

    </div>
</template>

<script>
export default {
  name : "MovieCard",
  props: {
    movieList: Array,
    // movie: Object,
  },
  created() {
    console.log(this.movieList)
  },
}
</script>

<style>
.text-style {
  display: inline-block;
  width: 300px;
  white-space: normal;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.5;
  height: 4.5;
}
</style>