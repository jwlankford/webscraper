// frontend/src/components/ResultsPage.vue
<script>
import { getScreenshots } from '@/services/api';

export default {
  props: ['url'], // Or however you are receiving the URL
  data() {
    return {
      screenshotsUrl: null,
      error: null,
    };
  },
  created() {
    this.fetchScreenshots();
  },
  methods: {
    async fetchScreenshots() {
      try {
        const data = await getScreenshots(this.url);
        this.screenshotsUrl = data.screenshot_url;
      } catch (err) {
        this.error = err.message || 'Failed to fetch screenshot.';
        console.error('Error fetching screenshot:', err);
      }
    },
  },
};
</script>

<template>
  <div>
    <h1>Scraping Results</h1>
    <div v-if="screenshotsUrl">
      <h2>Screenshot</h2>
      <img :src="screenshotsUrl" alt="Website Screenshot">
    </div>
    <div v-else-if="error">
      <p>Error: {{ error }}</p>
    </div>
    <div v-else>
      <p>Fetching screenshot...</p>
    </div>
    </div>
</template>

<style scoped>
img {
  max-width: 100%;
  height: auto;
}
</style>