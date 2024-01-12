"""
URL : https://sjmain.esunsec.com.tw/z/zg/zg_BD_1_0.djhtm
token : HLphngWSvoKdfrCdF3alRDOlvWBrLoZdlL2Ir54Fg5N
"""
import traceback
import pandas as pd
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from stock.股票抽籤LINE_Notify import report


def clean_strip(text):
    return text.replace("\xa0", "")


def get(url):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                      AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)
    soup = BeautifulSoup(html.text, 'html.parser')
    tags = soup.find_all('tr')
    time = soup.find('div', class_="t11")
    rows = []
    for tag in tags:
        row = []

        rank = tag.find('td', class_='t3n0', id="oAddCheckbox")  # 排名
        if not rank:
            continue

        name = tag.find('td', class_="t3t1")  # 名稱
        row.append(clean_strip(name.text.strip()))

        price = tag.find('td', class_="t3n1")  # 價格
        row.append(clean_strip(price.text.strip()))

        vol_and_turnover_rate_tags = tag.find_all('td', class_="t3n1")  # 成交量及週轉率

        if len(vol_and_turnover_rate_tags) == 3:
            volume = clean_strip(vol_and_turnover_rate_tags[1].text.strip())
            row.append(volume)

            turnover_rate = clean_strip(vol_and_turnover_rate_tags[2].text.strip())
            row.append(turnover_rate)

        rows.append(row)
    return rows, time


def trans_list(data):
    new_data = data[2:7]
    return new_data


def convert_pd(new_list):  # 已完成
    result_df = []
    # print(new_list)
    for step in range(len(new_list)):
        df_data = pd.DataFrame({
            'pack': new_list[step],
        }, index=[new_list[step]])
        result_df.append(df_data)
    combined_df = pd.concat(result_df)

    return combined_df


def write(new_list):  # 已完成
    df = convert_pd(new_list)
    file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/Turnover_DATA/DATA.txt'
    with open(file_path, 'w', encoding='UTF-8') as file:
        df.to_csv(file, index=False)


def notify(new_list, time):
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    # token = "tXTEUdyi4ULLp7HX7C8x6Tw6Kpwq0VIJJNywp1kX4CK"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    message = '\n\n'.join([' '.join(row) for row in new_list])
    data = {"message": f"\n資料{time.text}\n{message}"}
    resp = requests.post(url, headers=headers, data=data)
    if str(resp) != '<Response [200]>':
        report(__file__, resp)
    return resp


def data_dup(var1):
    file_df = pd.read_csv('/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/Turnover_DATA/DATA.txt', encoding='utf-8')
    data1 = file_df['pack'][0:len(file_df) + 1].tolist()
    # print(data1)
    for step in range(0, len(file_df)):
        # print(var1)
        if var1[step][0] == data1[step]:  # 判斷代號是否已在資料庫
            print('False')
            return False  # 重複
        else:
            # print(var1[step][0])
            # print(data1[step])
            # print('True')
            return True  # 不重複


def sort(arr):
    sort_arr = sorted(arr, key=lambda x: float(x[3][:-1]), reverse=True)
    return sort_arr


if __name__ == "__main__":
    data = []
    try:
        for i in range(0, 2):
            url = f'https://fubon-ebrokerdj.fbs.com.tw/z/zg/zg_BD_{i}_0.djhtm'
            result = get(url)
            time = result[1]
            for step in range(2, 7):
                data.append(result[0][step])
        # print(data)
        sort_data = sort(data)

        # data_list = trans_list(data)
        # data_dup(data_list)
        if data_dup(sort_data):
            resp = notify(sort_data, time)
            print(resp)
            if str(resp) == '<Response [200]>':  # 傳送成功寫入資料庫
                write(sort_data)

    except Exception as e:
        traceback.print_exc()
        report(__file__, traceback.format_exc())  # 回報主控台錯誤訊息內容，會觸發Notify，請小心使用
