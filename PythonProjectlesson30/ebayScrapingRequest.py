import requests

url="https://gjirafa50.com/search?q=laptop"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f" Failed to retrive content from {url}")
