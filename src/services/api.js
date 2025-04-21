// frontend/src/services/api.js

import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});

export const scrapeWebsite = async (url) => {
  try {
    const response = await apiClient.post('/scrape', { url });
    return response.data;
  } catch (error) {
    console.error('Error in scrapeWebsite:', error);
    throw error;
  }
};

export const getScreenshots = async (url) => {
  try {
    const response = await apiClient.get(`/screenshots?url=${encodeURIComponent(url)}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching screenshots:', error);
    throw error;
  }
};