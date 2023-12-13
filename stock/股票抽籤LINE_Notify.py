"""
url = 'https://histock.tw/stock/public.aspx'
截止日/價差/市場別/中籤率
名稱/
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime


def merge_list(number, state, new_lens, name, end_time, profit_reward, price, amount, rate):
    new_list = []
    for step in range(new_lens):
        if rate[step] == '0%':
            rate[step] = '尚未公告'
        new_list.append([
            f'{step + 1}.\n{number[step]} {name[step]}\n承銷價：{price[step]}*{amount[step]}張\n價差：{profit_reward[step]}'
            f'$\n截止日：{end_time[step]}\n狀態：{state[step]}\n中籤率：{rate[step]}'])
    # print(new_list)
    return new_list


def notify(data):
    number, state, lens, name, end_time, profit_reward, price, amount, rate = data

    def sent(message):
        url = "https://notify-api.line.me/api/notify"
        # token = "p9w0gHpW8GMAdin0YSdpq467C73swBi9h8rjzdcM7nA"  # TEST token
        token = "7ABygdMg7ZHO9B55ysAYlAJk28ZLJyHxdgJJJW1buIG"
        headers = {"Authorization": "Bearer " + token}
        data = {"message": f'\n{message}\n**此為自動推播**\n**請以公告為主**'}
        resp = requests.post(url, headers=headers, data=data)
        return resp

    if lens == 0:  # 無新資料
        message = f'今天是{datetime.now().date()}\n沒有即將開始的抽籤標的喔'
        sent(message)
        return False
    else:
        new_list = merge_list(number, state, lens, name, end_time, profit_reward, price, amount, rate)
        message = f'\n\n\n資料時間：{datetime.now().date()}\n'.join([' '.join(row) for row in new_list])
        sent(message)
        return True


def convert_pd(number, state):  # 已完成
    result_df = []
    for step in range(len(number)):
        df_data = pd.DataFrame({
            'number': number[step],
            'state': state[step]
        }, index=[number[step]])
        result_df.append(df_data)
    combined_df = pd.concat(result_df)

    return combined_df


def write(number, state):  # 已完成
    df = convert_pd(number, state)
    file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/股票抽籤DATA/DATA.txt'
    with open(file_path, 'w', encoding='UTF-8') as file:
        df.to_csv(file, index=False)


def get(url_get):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                          AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url_get, headers=chrome_headers)
    soup = BeautifulSoup(html.text, 'html.parser')

    # state = soup.select('td' > 'span:not[style !="color:gray;"]')  # CSS選擇器，但會抓到非目標資料
    state_data = soup.find_all('td', style="font-weight:bold;width:67px;")
    lens, state = 0, []
    for step in range(2, len(state_data), 3):
        state_cache = state_data[step]

        span_data = state_cache.find_all('span', style="color:gray;")

        if any(span.text.strip() == "已截止" for span in span_data):
            # state.append('已截止')  # 抓去舊資料請打開這裏並把break改成continue，迴圈外直接定義lens={需要的資料長度}
            break

        if state_cache.text.strip() == "":
            state.append("尚未開始")
        else:
            state.append(state_cache.text.strip())

        lens += 1

    name_data = soup.find_all('a', href=re.compile(r'/stock/(\d+)'), target='_blank', title=False)
    name, number = [], []
    for step in range(lens):
        number.append(name_data[step].text.split('\xa0')[0])
        name.append(name_data[step].text.split('\xa0')[1])

    market_type_data = soup.find_all('td', style="width:70px;")
    market_type = []
    for step in range(lens):
        market_type.append(market_type_data[step].text.strip())

    profit_data = soup.find_all('span', class_="clr-rd")
    profit_reward, profit_percent = [], []
    for step in range(0, lens * 2, 2):
        profit1, profit2 = profit_data[step].text.strip(), profit_data[step + 1].text.strip()
        profit_reward.append(profit1)
        profit_percent.append(profit2)

    time_data = soup.find_all('td', style="width:100px;")
    start_time, end_time = [], []
    for step in range(lens):
        start_time.append(time_data[step].text.strip().split('~')[0])
        end_time.append(time_data[step].text.strip().split('~')[1])

    td_width67px = soup.find_all('td', style="width:67px;")
    price, amount, rate = [], [], []
    for step in range(2, lens * 6, 6):  # 承銷價 OK
        price.append(td_width67px[step].text.strip())

    for step in range(3, lens * 6, 6):  # 抽籤張數 OK
        amount.append(td_width67px[step].text.strip())

    for step in range(5, lens * 6, 6):  # 中籤率 OK
        rate.append(f'{td_width67px[step].text.strip()}%')

    return number, state, lens, name, end_time, profit_reward, price, amount, rate


if __name__ == "__main__":
    url = 'https://histock.tw/stock/public.aspx'
    data = get(url)  # 去的資料
    resp = notify(data)

    if resp:  # 傳送成功寫入資料庫
        write(*data[:2])
