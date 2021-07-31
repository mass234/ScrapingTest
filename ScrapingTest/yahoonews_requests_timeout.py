import requests

url = 'https://news.yahoo.co.jp'
response = requests.get(url,timeout = 3)
response.text

print(response.text)