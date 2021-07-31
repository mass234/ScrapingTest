import requests
from bs4 import BeautifulSoup

result = requests.get('https://newspicks.com/') 
data_1 = BeautifulSoup(r.text, 'html.parser')
data_2 = data.find_all("div", class_="title _ellipsis")

for item in data_2:
 print(item.getText())


