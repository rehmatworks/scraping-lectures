import requests
from bs4 import BeautifulSoup
import os


BASE_URL = 'https://placeholder.com/stock-photos/'

res = requests.get(BASE_URL)

if res.status_code:
    soup = BeautifulSoup(res.text, 'html.parser')
    
    link_elements = soup.find_all('a')
    image_elements = soup.find_all('img')
    
    # Store links and images in a list
    links = []
    images = []
    
    # <a href="https://google.com">Google</a>
    
    if len(link_elements):
        for link in link_elements:
            links.append(link['href'])
            
    # <img src="https://test.com/image.png" alt="test tag"/>
    if len(image_elements):
        for img in image_elements:
            try:
                images.append(img['src'])
            except KeyError:
                pass

    # Remove duplicates
    links = list(set(links))
    images = list(set(images))
    
    # Download images
    print(f'Downloading {len(images)} images.')
    
    # Images storage path
    # BASE_IMAGE_PATH = '/Users/rehmat/sites/scraping-lectures/day2/images'
    # Use current directory to store images in
    BASE_IMAGE_PATH = os.path.join(os.getcwd(), 'images')
    
    # Check if directory exists, if not, create it
    if not os.path.exists(BASE_IMAGE_PATH):
        os.makedirs(BASE_IMAGE_PATH)
    
    for img_link in images:
        image_name = os.path.basename(img_link)
        image_path = os.path.join(BASE_IMAGE_PATH, image_name)
        
        if os.path.exists(image_path):
            print(f'Image {image_name} already downloaded.')
        else:
            # Get the image
            res = requests.get(img_link)
            
            
            if res.status_code == 200:
                with open(image_path, 'wb') as f:
                    f.write(res.content)
            else:
                print(f'Can\'t download image from {img}')
                
    
    for img in images:
        if len(images)