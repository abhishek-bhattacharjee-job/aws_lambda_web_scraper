import json

import requests
from bs4 import BeautifulSoup

def scrapper_BeautifulSoup(url):
    print("------------scrapper_BeautifulSoup")
    print(url)
    response = requests.get(url, timeout=60)
    print(response)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        return text
    else:
        print('Error:', response.status_code)
        return None

def lambda_handler(event, context):
    req_data = json.loads(event["body"])
    url = req_data["url"]
    website_text = scrapper_BeautifulSoup(url)
    return {
        'statusCode': 200,
        'body': json.dumps({ "scraped_data" : website_text})
    }
