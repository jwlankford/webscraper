<template>
    <div class="home">
      <h1>Website Scraper</h1>
      <form @submit.prevent="submitUrl">
        <input
          v-model="url"
          type="text"
          placeholder="Enter URL here"
          required
        />
        <button type="submit">Scrape</button>
      </form>
    </div>
  </template>
  
  <script>
  import { scrapeWebsite } from "@/services/api";
  
  export default {
    name: "HomePage",
    data() {
      return {
        url: "",
      };
    },
    methods: {
      async submitUrl() {
        try {
          await scrapeWebsite(this.url);
          this.$router.push("/results"); // Redirect to Results page
        } catch (error) {
          console.error("Error submitting URL:", error);
        }
      },
    },
  };
  </script>
  