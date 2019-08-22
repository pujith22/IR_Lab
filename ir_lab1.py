import requests
from bs4 import BeautifulSoup
import re
url = "https://en.wikipedia.org/wiki/Main_Page"
html = requests.get(url).content
soup = BeautifulSoup(html)
for link in soup.findAll('a', attrs={'href':re.compile("^https://")}):
    print(link.get('href'))