import requests

url = 'https://news.yahoo.co.jp'
response = requests.get(url)
response.status_code

print(response.status_code)