import requests

url = 'https://news.yahoo.co.jp'
response = requests.get(url)
response.encoding

print(response.encoding)