from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
import requests
import pymongo

app = Flask(__name__)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['catalog']
collection = db['products']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    product_name = request.form['product']
    # Assuming you scrape data here and store it in MongoDB
    products = collection.find({"name": {"$regex": product_name, "$options": "i"}})
    return jsonify([product for product in products])

if __name__ == "__main__":
    app.run(debug=True)
