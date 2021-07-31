from bs4 import BeautifulSoup
from urllib.request import urlopen
response = urlopen('https://www.naver.com/')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.find_all('a'):
    print(anchor.get_text())
    # print(anchor)
    # print(anchor.get('href', '/'))
    
    