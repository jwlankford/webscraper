from flask import Flask, request, jsonify
from scrape import scrape_website
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Initialize CORS for your app

@app.route('/scrape', methods=['POST'])
def scrape():
    data = request.json
    url = data.get('url')
    output_folder = data.get('folder', 'screenshots')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        screenshot_path = scrape_website(url, output_folder)
        return jsonify({"message": "Screenshot saved", "path": screenshot_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
