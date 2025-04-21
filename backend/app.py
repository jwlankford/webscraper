# backend/app.py
import os
import time
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

app = Flask(__name__)
CORS(app)
app.config['SCREENSHOTS_FOLDER'] = 'screenshots'
os.makedirs(app.config['SCREENSHOTS_FOLDER'], exist_ok=True)

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        time.sleep(2)

        title = driver.find_element(By.TAG_NAME, 'h1').text.strip() if driver.find_elements(By.TAG_NAME, 'h1') else "No title found"
        paragraphs = [p.text.strip() for p in driver.find_elements(By.TAG_NAME, 'p')]

        driver.quit()
        return jsonify({'title': title, 'paragraphs': paragraphs})
    except Exception as e:
        if "invalid argument" in str(e):
            return jsonify({'error': f'Invalid argument during scraping: {str(e)}'}), 500
        else:
            return jsonify({'error': f'Error during scraping: {str(e)}'}), 500

@app.route('/screenshots')
def get_screenshot():
    url = request.args.get('url')
    if not url:
        return jsonify({'error': 'URL parameter is required'}), 400

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1280, 720)
        driver.get(url)
        time.sleep(2)

        filename = f"screenshot_{time.time()}.png"
        filepath = os.path.join(app.config['SCREENSHOTS_FOLDER'], filename)
        driver.save_screenshot(filepath)
        driver.quit()
        return jsonify({'screenshot_url': f'/screenshots/{filename}'})
    except Exception as e:
        return jsonify({'error': f'Error taking screenshot: {str(e)}'}), 500

@app.route('/screenshots/<path:filename>')
def serve_screenshot(filename):
    return send_from_directory(app.config['SCREENSHOTS_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)