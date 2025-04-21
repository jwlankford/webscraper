const BASE_URL = 'http://127.0.0.1:5000'; // Replace with your actual base URL

export async function scrapeWebsite(url, folder = 'screenshots') {
  try {
    const response = await fetch(`${BASE_URL}/scrape`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url, folder }),
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.error || 'An error occurred while scraping');
    }

    return await response.json();
  } catch (error) {
    console.error('Error in scrapeWebsite:', error);
    throw error;
  }
}
