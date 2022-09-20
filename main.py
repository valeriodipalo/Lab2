import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find('table').find_all('tr')

tickers = []
for tr in table:
  tickers.append(tr.find('a').text)

tickers = tickers[1:]
print(tickers)



