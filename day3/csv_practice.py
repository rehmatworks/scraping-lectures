import requests
from bs4 import BeautifulSoup
import os
import csv
from fake_useragent import UserAgent

# Define base URL
BASE_URL = 'http://musicguide.com.pk/'

# Construct headers
ua = UserAgent()
HEADERS = {
    'user-agent': ua.random
}

# Make an HTTP request and get back the HTML
resp = requests.get(BASE_URL, headers=HEADERS)

if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, 'html.parser')
    products = []
    # Target by class name: grid-item
    product_elements = soup.find_all('div', {'class': 'grid-item'})
    for prod in product_elements:
        try:
            price = prod.find('span', {'class': 'price-top'}).text
        except AttributeError:
            price = prod.find('span', {'class': 'price-new'}).text
        
        single_prod = [
            prod.find('h3').text,
            price,
            prod.find('img')['src']
        ]
        
        products.append(single_prod)
    
    
    
    # Write CSV
    CSV_PATH = os.path.join(os.getcwd(), 'products-data.csv')
    
    with open(CSV_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Product Name', 'Price', 'Image URL'])
        
        # Loop through products
        for prod in products:
            writer.writerow(prod)
        
        
    
    
