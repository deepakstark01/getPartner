from bs4 import BeautifulSoup
import requests, re, json
import time
from collections import OrderedDict
from flask import Flask,request, jsonify
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, origins=["https://uibob.sddoc.in", "http://localhost:3000","http://localhost:3000/" ,"https://improved-yodel-jw6rgqjg4gv35r79-3000.app.github.dev", "https://glorious-space-dollop-rq964wvjrpq356pq-3000.app.github.dev"])

@app.route('/')
def index():
    htmlindex = """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Bol.com Scraper</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
</head>

<body class="bg-gray-100">
    <div class="container mx-auto p-4">
        <h1 class="text-3xl font-bold text-center mt-8 mb-6">Welcome Bob to the Bol.com Scraper</h1>

        <div class="flex justify-center">
            <a href="/getdata?page=1&querry=charger"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                Get Data
            </a>
        </div>
    </div>
</body>

</html>

    """

    return htmlindex 

def getpartner(url):
    while True:
        response= requests.get(url)
        if response.status_code != 200:
            time.sleep(2)
            continue
        partnerSoup = BeautifulSoup(response.text, 'html.parser')
        target_div = partnerSoup.find('div', class_='buy-block__alternative-sellers-card__title', string=lambda text: 'partners' in text.lower())
        if target_div :
            try:
                NumOfpartners = target_div.text.strip()
                return str(NumOfpartners)
                
            except:
                NumOfpartners = 1
                return str(NumOfpartners)
                
        

@app.route('/getdata')
def get_data():
    url = request.args.get('url')
    if not url:
        return "Error: Missing 'url' parameter", 400
    
    return getpartner(url)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
