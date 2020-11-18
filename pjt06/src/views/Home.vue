<template>
  <div class="home">
    <!-- <MovieCard
      v-for="movie in movieList"
      :key="movie.id"
      :movie="movie"
    /> -->
    <MovieCard
      :movieList="movieList"
    />
  </div>
</template>

<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const API_URL = 'https://gist.githubusercontent.com/eduChange-hphk/756c987fe4ecf20ef27fd1d29f90764e/raw/f5a6acfed6bbe837d7f2f173a5b84221ee54c3b2/movies.json'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  data() {
    return {
      movieList: [],
    }
  },
  created() {
    this.fetchMovieList()
  },
  methods: {
    fetchMovieList() {
      axios.get(API_URL)
      .then(res => {
        this.movieList = res.data
        console.log(this.movieList)
      })
      .catch(err => {
        console.error(err)
      })
    },
  },
}
</script>
