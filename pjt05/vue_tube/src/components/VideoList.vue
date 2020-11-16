<template>
  <div class="videoList">
    <VideoListItem
      v-for="video in videoList"
      :key="video.etag"
      :video="video"
      @select-video="selectVideo"
    />
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videoList: Array,
  },
  methods: {
    selectVideo(video) {
      this.$emit('select-video', video)
      console.log('selectedVideo from VideoList')
    }
  },
}
</script>

<style scoped>
.videoDetail {
  width: 30%;
}
</style>