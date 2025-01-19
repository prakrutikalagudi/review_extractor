from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

def scrape_reviews(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, timeout=10, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        reviews = []
        
        for item in soup.find_all("div", class_="col EPCmJX Ma1fCG"):
            title = item.select_one('p.z9E0IG')
            body = item.select_one("div.ZmyHeo")
            rating = item.select_one('div.XQDdHH')
            reviewer = item.select_one('p.AwS1CA')
            
            reviews.append({
                'title': title.text.strip() if title else "No Title",
                'review_body': body.text.strip() if body else "No Body",
                'rating': rating.text.strip() if rating else "No Rating",
                'reviewer': reviewer.text.strip() if reviewer else "Anonymous"
            })
        return reviews, None
    except Exception as e:
        return None, str(e)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    reviews, error = scrape_reviews(url)
    if error:
        return jsonify({'error': error}), 500
    
    return jsonify({'reviews': reviews})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
