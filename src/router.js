// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../components/HomePage.vue';
import ResultsPage from '../components/ResultsPage.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage,
  },
  {
    path: '/results',
    name: 'Results',
    component: ResultsPage,
    props: route => ({ url: route.query.url }), // Pass the URL as a prop
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;