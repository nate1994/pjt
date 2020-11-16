<template>
  <div class="videoDetail">
    <div class="videoContainer">
      <iframe 
        :src="videoUrl" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen
      >
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'VideoListItemDetail',
  props: {
    video: Object,
  },
  computed: {
    videoUrl() {
      const videoId = this.video.id.videoId
      const Url = `https://www.youtube.com/embed/${videoId}`
      return Url
    }
  },
}
</script>

<style>
.videoDetail {
  width: 70%;
  padding-right: 1rem;
}

.videoContainer {
  position: relative;
  padding-top: 56.25%;
}

.videoContainer > iframe {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
}
</style>

