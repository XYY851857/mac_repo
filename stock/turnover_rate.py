"""
URL : https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm
token : HLphngWSvoKdfrCdF3alRDOlvWBrLoZdlL2Ir54Fg5N
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re


def clean_strip(text):
    return text.replace("\xa0", "")


def get(url):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                      AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)
    # print('HTML:', html)
    soup = BeautifulSoup(html.text, 'html.parser')
    # print('soup', soup)
    pattern = re.compile(r'javascript:Link2Stk(\'\d\')')
    tags = soup.find_all('tr')
    print('len(tags)', len(tags))
    # print(tags)
    rows = []
    for tag in tags:
        row = []

        rank = tag.find('td', class_='t3n0', id="oAddCheckbox")
        if not rank:
            continue
        # row.append(rank.text)
        row.append(clean_strip(rank.text.strip()))
        # print(rank.text)

        name = tag.find('td', class_="t3t1")
        row.append(clean_strip(name.text.strip()))
        # print(name.text)

        price = tag.find('td', class_="t3n1")
        row.append(clean_strip(price.text.strip()))
        # print(price.text)

        vol_and_turnover_rate_tags = tag.find_all('td', class_="t3n1")

        if len(vol_and_turnover_rate_tags) == 3:
            volume = clean_strip(vol_and_turnover_rate_tags[1].text.strip())
            row.append(volume)
            # print(volume)

            turnover_rate = clean_strip(vol_and_turnover_rate_tags[2].text.strip())
            row.append(turnover_rate)
            # print(turnover_rate)

        rows.append(row)
    return rows


def notify():  # 未完成 =.='
    url = "https://notify-api.line.me/api/notify"
    token = "HLphngWSvoKdfrCdF3alRDOlvWBrLoZdlL2Ir54Fg5N"


if __name__ == "__main__":
    url = 'https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm'
    data = get(url)
    print(data)
"""
待辦事項：
data資料前2個去掉
連動LINE Notify

注意事項：
抓資料測試OK
"""