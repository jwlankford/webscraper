// frontend/src/components/HomePage.vue
<script>
import { scrapeWebsite } from '@/services/api';

export default {
  data() {
    return {
      urlToScrape: '',
      errorMessage: '',
      scrapingResult: null,
    };
  },
  methods: {
    async submitUrl() {
      try {
        this.errorMessage = '';
        this.scrapingResult = await scrapeWebsite(this.urlToScrape);
        console.log('Scrape Result:', this.scrapingResult);
        // Navigate to the results page, passing the URL
        this.$router.push({ name: 'Results', query: { url: this.urlToScrape } });
      } catch (error) {
        console.error('Error submitting URL:', error);
        this.errorMessage = error.message;
        this.scrapingResult = null;
      }
    },
  },
};
</script>