"""
URL : https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm
token : HLphngWSvoKdfrCdF3alRDOlvWBrLoZdlL2Ir54Fg5N
"""
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


def clean_strip(text):
    return text.replace("\xa0", "")


def get():
    url = 'https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm'
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
    time = soup.find('div', class_="t11")
    print(time.text)
    rows = []
    for tag in tags:
        row = []

        rank = tag.find('td', class_='t3n0', id="oAddCheckbox")  # 排名
        if not rank:
            continue
        # row.append(rank.text)
        # row.append(clean_strip(rank.text.strip()))
        # print(rank.text)

        name = tag.find('td', class_="t3t1")  # 名稱
        row.append(clean_strip(name.text.strip()))
        # print(name.text)

        price = tag.find('td', class_="t3n1")  # 價格
        row.append(clean_strip(price.text.strip()))
        # print(price.text)

        vol_and_turnover_rate_tags = tag.find_all('td', class_="t3n1")  #成交量及週轉率

        if len(vol_and_turnover_rate_tags) == 3:
            volume = clean_strip(vol_and_turnover_rate_tags[1].text.strip())
            row.append(volume)
            # print(volume)

            turnover_rate = clean_strip(vol_and_turnover_rate_tags[2].text.strip())
            row.append(turnover_rate)
            # print(turnover_rate)

        rows.append(row)
    return rows, time


def trans_list(data):
    new_data = data[2:12]
    return new_data


def notify(my_list, time):
    new_list = trans_list(my_list)
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    # token = "p9w0gHpW8GMAdin0YSdpq467C73swBi9h8rjzdcM7nA"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    message = '\n\n'.join([' '.join(row) for row in new_list])
    print(new_list)
    print(message)

    data = {"message": f"\n資料{time.text}\n{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


if __name__ == "__main__":
    data, time = get()
    resp = notify(data, time)
    # print(data)
    print(resp)
