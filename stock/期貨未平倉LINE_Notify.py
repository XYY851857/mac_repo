"""
url : "https://tw.stock.yahoo.com/future/futures_uncovered.html"
token : "jn41HsUfAyRN3intXow0qL4LpjpoyNfIiQhXSJe8apM"
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def clean_strip(text):
    return ''.join(text.split())


def get(url):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                          AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup)
    num = soup.find_all('font', color='blue')
    dealer = clean_strip(num[5].text)
    investment_trust = clean_strip(num[11].text)
    foreign_investment = clean_strip(num[17].text)
    return dealer, investment_trust, foreign_investment


def notify(dealer, investment_trust, foreign_investment, time):
    url = "https://notify-api.line.me/api/notify"
    token = "jn41HsUfAyRN3intXow0qL4LpjpoyNfIiQhXSJe8apM"
    headers = {"Authorization": "Bearer " + token}
    message = f'\n資料擷取時間：{time}\n外資{foreign_investment:.6}\n投信{investment_trust}\n自營商{dealer}'

    data = {"message": message}
    resp = requests.post(url, headers=headers, data=data)
    return resp


if __name__ == "__main__":
    url = "https://www.taifex.com.tw/cht/3/futContractsDate"
    token = "jn41HsUfAyRN3intXow0qL4LpjpoyNfIiQhXSJe8apM"
    time = (datetime.now()).strftime("%Y/%m/%d")
    dealer, investment_trust, foreign_investment = get(url)
    resp = notify(dealer, investment_trust, foreign_investment, time)
