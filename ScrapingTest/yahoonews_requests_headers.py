import requests

url = 'https://news.yahoo.co.jp'
response = requests.get(url)
response.headers

for key,value in response.headers.items():
    print(key,'   ',value)