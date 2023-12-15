"""
URL : https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm
token : HLphngWSvoKdfrCdF3alRDOlvWBrLoZdlL2Ir54Fg5N
"""
import pandas as pd
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
    # print('len(tags)', len(tags))
    # print(tags)
    time = soup.find('div', class_="t11")
    # print(time.text)
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

        vol_and_turnover_rate_tags = tag.find_all('td', class_="t3n1")  # 成交量及週轉率

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


def convert_pd(new_list):  # 已完成
    result_df = []
    print(new_list)
    for step in range(len(new_list)):
        df_data = pd.DataFrame({
            'pack': new_list[step],
        }, index=[new_list[step]])
        result_df.append(df_data)
    combined_df = pd.concat(result_df)
    # print(combined_df)

    return combined_df


def write(new_list):  # 已完成
    df = convert_pd(new_list)
    file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/Turnover_DATA/DATA.txt'
    with open(file_path, 'w', encoding='UTF-8') as file:
        df.to_csv(file, index=False)


def notify(new_list, time):
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    # token = "p9w0gHpW8GMAdin0YSdpq467C73swBi9h8rjzdcM7nA"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    message = '\n\n'.join([' '.join(row) for row in new_list])
    data = {"message": f"\n資料{time.text}\n{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


def data_dup(var1):
    file_df = pd.read_csv('/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/Turnover_DATA/DATA.txt', encoding='utf-8')
    data1 = file_df['pack'][0:len(file_df) + 1].tolist()
    for step in range(0, len(file_df)):
        if var1[step][0] == data1[step]:  # 判斷代號是否已在資料庫
            # print('False')
            return False  # 重複
        else:
            # print(var1[step][0])
            # print(data1[step])
            # print('True')
            return True  # 不重複


if __name__ == "__main__":
    data, time = get()
    data_list = trans_list(data)
    # data_dup(data_list)
    if data_dup(data_list):
        resp = notify(data_list, time)
        # print(resp)
        if resp:  # 傳送成功寫入資料庫
            write(data_list)
