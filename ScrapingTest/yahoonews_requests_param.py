import requests

url = 'https://www.google.co.jp/search'
param = {'q': 'initial d'}
response = requests.get(url,params = param)
response.text

print(response.text)