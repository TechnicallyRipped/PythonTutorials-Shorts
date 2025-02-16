

# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h3')
    for title in titles:
        print(title.a['title'])
    
    
    
