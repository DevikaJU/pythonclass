import requests
from bs4 import BeautifulSoup
URL = "https://books.toscrape.com/"
req = requests.get(URL)
source_code = req.content
soup = BeautifulSoup(source_code,'lxml')
article = soup.find_all('article')
for i in article:
    rows = i.find_all('h3')
    print(rows)


