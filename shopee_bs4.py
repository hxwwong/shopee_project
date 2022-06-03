import bs4 
import requests 
from lxml import etree
from bs4 import BeautifulSoup 

URL = 'https://shopee.ph/search?keyword=xda%20keycaps'
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'lxml')
# print(soup.prettify())

# searching for content 

