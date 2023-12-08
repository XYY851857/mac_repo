"""
url = 'https://histock.tw/stock/public.aspx'
token = 'SFJszrFZMHievEBqql9GFFSU29PtoMdwgeEOH84CX6c'
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import re


def notify(my_list, time):
    new_list = trans_list(my_list)
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    headers = {"Authorization": "Bearer " + token}
    message = '\n\n'.join([' '.join(row) for row in new_list])

    data = {"message": f"\n資料{time.text}\n{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


def get(url_get):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                          AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }

    html = requests.get(url_get, headers=chrome_headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup)
    name = soup.find_all('a', href=re.compile(r'/stock/(\d+)'), target='_blank', title=False)
    print(name[0].text)

    deadline = soup.find_all('td', style="width:100px;")
    print(deadline[0].text.strip().split('~')[1])

    market_type = soup.find_all('td', style="width:70px;")
    print(market_type[0].text.strip())

    profit_data = soup.find_all('span', class_="clr-rd")
    profit_reward, profit_percent = [], []
    for step in range(0, len(profit_data), 2):
        profit1, profit2 = profit_data[step].text.strip(), profit_data[step + 1].text.strip()
        profit_reward.append(profit1)
        profit_percent.append(profit2)
    print(profit_reward[0])
    print(profit_percent[0])

    # state = soup.select('td' > 'span:not[style !="color:gray;"]')  # CSS選擇器，但會抓到非目標資料
    state_data = soup.find_all('td', style="font-weight:bold;width:67px;")
    lens, state = 0, []
    for step in range(2, len(state_data), 3):
        state_cache = state_data[step]
        for span in state_cache.find_all('span', style="color:gray;"):  # 可能會有bug
            if span.text.strip() == "已截止":
                break
        else:
            if state_cache == "\n":
                state.append("尚未開始")
                lens += 1
                continue
            else:
                state.append(f'{lens}{state_cache}')
                lens += 1
                continue
        break
    print(lens)
    print(state)

    return name, deadline, market_type, profit_reward, profit_percent, lens


if __name__ == "__main__":
    url = 'https://histock.tw/stock/public.aspx'
    token = 'SFJszrFZMHievEBqql9GFFSU29PtoMdwgeEOH84CX6c'
    data = get(url)
    # resp = notify(*data)
