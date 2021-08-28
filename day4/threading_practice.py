# Import grequests
import grequests
import requests
import time
from bs4 import BeautifulSoup

import sys


# URLs list
TOTAL_PAGES = 13

# Build a pages list
URLS_LIST = []
for page in range(1, (TOTAL_PAGES) + 1):
    url = f'https://goodapks.com/page/{page}/?s='
    URLS_LIST.append(url)
    

# Send requests one at a time
time_start = time.time()
for url in URLS_LIST:
    print(f'Getting URL {url}')
    res = requests.get(url)
    
time_end = time.time()
time_taken = float(time_end - time_start)
print(f'Single requests: It took {time_taken} to process {TOTAL_PAGES}')


# Use grequests to send multiple requests together
GREQ_URLS = []
time_start = time.time()
for url in URLS_LIST:
    GREQ_URLS.append(grequests.get(url))

# Send requests
responses = grequests.map(GREQ_URLS)
for response in responses:
    soup = BeautifulSoup(response.text, 'html.parser')
    els = soup.find_all('div', {'class': 'app-info'})
    for el in els:
        print(el.find('a').text)

time_end = time.time()
time_taken = float(time_end - time_start)
print(f'Multiple requests: It took {time_taken} to process {TOTAL_PAGES}')
