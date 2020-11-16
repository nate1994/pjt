<template>
  <div>
    <input class="searchBar" type="text" @keypress.enter="fetchVideos">
  </div>
</template>

<script>
import axios from 'axios'

const BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

export default {
  name: 'SearchBar',
  data() {
    return {
      userInput: '',
    }
  },
  methods: {
    fetchVideos(event) {
      this.userInput = event.target.value

      const config = {
        // 객체로 바깥을 한번더 감싼 이유는 params이외에 다른 속성도 있기때문
        params: {
          part: 'snippet',
          key: API_KEY,
          q: this.userInput,
        },
      }
      axios.get(BASE_URL, config)
      .then(res => {
        console.log(res)
        this.$emit('selected-videos', res.data.items)
      })
      .catch(err => {
        console.error(err)
      })
    },
  },
}
</script>

<style scoped>
.searchBar {
  width: 100%;
  padding: 0.5rem;
  font-size: 1.25rem;
}
</style>