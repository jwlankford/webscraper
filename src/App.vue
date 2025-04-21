<template>
  <div id="app">
    <router-view /> <!-- This dynamically loads the current route's component -->
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Global styles */
#app {
  font-family: Arial, sans-serif;
  text-align: center;
  margin-top: 20px;
}
</style>
