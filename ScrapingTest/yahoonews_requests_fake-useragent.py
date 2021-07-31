from fake_useragent import UserAgent
import requests

ua = UserAgent()
header = {'user-agent':ua.chrome}
response = requests.get('https://news.yahoo.co.jp',headers=header)

#url = 'https://news.yahoo.co.jp'
#response = requests.get(url)
#response.content[:500]
#response.cookies


#print(response.cookies)