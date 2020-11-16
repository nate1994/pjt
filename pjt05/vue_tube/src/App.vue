<template>
  <div id="app">
    <header>
      <SearchBar @selected-videos="selectedVideos"/>
    </header>
    <section>
      <VideoListItemDetail v-if="isVideoSelected" :video="selectedVideo"/>
      <VideoList :videoList="videoList" @select-video="selectVideo"/>
    </section>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoListItemDetail from '@/components/VideoListItemDetail'


export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoListItemDetail,
  },
  data() {
    return {
      videoList: [],
      selectedVideo: {},
      isVideoSelected: false,
    }
  },
  methods: {
    selectedVideos(videoList) {
      console.log(videoList)
      this.videoList = videoList
    },
    selectVideo(video) {
      this.selectedVideo = video
      this.isVideoSelected = true
      console.log(video)
      console.log('selectedVideo 호출!')
    }
  }
}
</script>

<style scoped>
header, section {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex;
}
</style>
