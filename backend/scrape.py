from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

def scrape_website(url, output_folder):
    # Set up the Chrome driver using webdriver-manager
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Navigate to the URL
    driver.get(url)

    # Take a screenshot
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    screenshot_path = os.path.join(output_folder, "screenshot.png")
    driver.save_screenshot(screenshot_path)

    driver.quit()

    return screenshot_path