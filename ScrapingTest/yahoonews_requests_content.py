import requests

url = 'https://news.yahoo.co.jp'
response = requests.get(url)
#response.content[:500]
response.content


print(response.content)