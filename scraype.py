from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text,features="html.parser")
#headers = soup.find_all('h2')
headers = soup.find_all('div',{'class': 'introduction'})
print(headers[0].text)