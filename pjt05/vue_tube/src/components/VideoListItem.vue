<template>
  <div @click="onSelectVideo">
    <img width=360 :src="thumbnailUrl(video)" alt="">
    <div>
      <div class="videoListItem__title">{{ video.snippet.title | unescape }}</div>
      <div class="videoLIstItem__channelTitle">{{ video.snippet.channelId }}</div>
      <div class="videoListItem__description">{{ video.snippet.description }}</div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    thumbnailUrl(video) {
      return video.snippet.thumbnails.high.url
    },
    onSelectVideo() {
      this.$emit('select-video', this.video)
    },
  },
  filters: {
    unescape(value) {
      return _.unescape(value)
    }
  },
}
</script>

<style scoped>
.videoListItem {
  display: flex;
}
.videoListItem__title {
  font-size: 1.25rem;
  font-weight: bold;
}
</style>