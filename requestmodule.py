from bs4 import BeautifulSoup
from requests import get

url = 'http://www.moneycontrol.com'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(type(soup))
print(soup.html.head.meta)

div = soup.find_all('table', class_='rhsglTbl')
#
print(div)
links = soup.find_all('a')
print(links)
