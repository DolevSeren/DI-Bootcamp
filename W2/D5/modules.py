import requests
import time


def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time

    if response.status_code == 200:
        print(f"Page {url} loaded successfully in {load_time:.4f} seconds.")
    else:
        print(f"Failed to load page {url}. Status code: {response.status_code}")



urls = ['https://www.google.com', 'https://www.ynet.co.il', 'https://www.imdb.com']

for url in urls:
    measure_load_time(url)
