"""
url : "https://tw.stock.yahoo.com/future/futures_uncovered.html"
token : "jn41HsUfAyRN3intXow0qL4LpjpoyNfIiQhXSJe8apM"
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get(url):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                          AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup)
    data = soup.find_all('td')
    print(data)




if __name__ == "__main__":
    url = "https://www.macromicro.me/charts/136/tw-future-stock"
    token = "jn41HsUfAyRN3intXow0qL4LpjpoyNfIiQhXSJe8apM"
    data = get(url)
