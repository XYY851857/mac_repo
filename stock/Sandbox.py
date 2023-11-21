# 網路位址 https://tw.stock.yahoo.com/quote/{}
# <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)">77.9</span>

import requests
from bs4 import BeautifulSoup


def get_stock_price(stock_no):
    url = 'https://tw.stock.yahoo.com/quote/{}'.format(stock_no)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    tag_name = 'span'
    class_value = 'Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)'
    tag = soup.find(name=tag_name, attrs={'class': class_value})
    # print(tag)
    return tag.text


if __name__ == '__main__':
    price = get_stock_price('2330')
    print(price)