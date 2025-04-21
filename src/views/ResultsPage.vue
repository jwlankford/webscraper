<template>
    <div class="results">
      <h1>Screenshots</h1>
      <div class="images-container">
        <div v-for="(image, index) in images" :key="index">
          <img :src="image" :alt="'Screenshot ' + (index + 1)" />
        </div>
      </div>
      <button @click="goBack">Back</button>
    </div>
  </template>
  
  <script>
  import { getScreenshots } from "@/services/api";
  
  export default {
    name: "ResultsPage",
    data() {
      return {
        images: [],
      };
    },
    async created() {
      try {
        const response = await getScreenshots();
        this.images = response.data.images;
      } catch (error) {
        console.error("Error fetching screenshots:", error);
      }
    },
    methods: {
      goBack() {
        this.$router.push("/");
      },
    },
  };
  </script>
  