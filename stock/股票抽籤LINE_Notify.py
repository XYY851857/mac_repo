"""
url = 'https://histock.tw/stock/public.aspx'
token = 'SFJszrFZMHievEBqql9GFFSU29PtoMdwgeEOH84CX6c'
截止日/價差/市場別/中籤率
名稱/
"""
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import re
from datetime import datetime


def notify(number, state, lens, name, end_time, profit_reward):  # 未完成
    new_list = trans_list(my_list)
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    headers = {"Authorization": "Bearer " + token}
    message = '\n\n'.join([' '.join(row) for row in new_list])

    data = {"message": f"\n資料時間：{datetime.now().date()}\n{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


def data_dup(get_number, get_state, ori_lens):  # NOTE:  lens = 3  已完成
    file_df = pd.read_csv('/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/股票抽籤DATA/DATA.txt', encoding='utf-8')
    number_data = file_df['number'][0:ori_lens + 1].tolist()
    state_data = file_df['state'][0:ori_lens + 1].tolist()
    new_lens = 0
    # print(set(number_data))
    # print(type(number_data[0]), type(state_data[2]))
    for slow_step in range(0, ori_lens):  # 慢指針
        if int(get_number[slow_step]) not in set(number_data):  # 判斷代號是否已在資料庫
            new_lens += 1
            continue
        else:  # 代號和資料庫重複
            for fast_step in range(len(state_data)): # 快指針，定位number重複的位置並比對state是否相同
                if get_number[slow_step] == number_data[fast_step] and get_state[fast_step] != state_data[fast_step]:
                    new_lens += 1

    print(f'{get_number}\n{number_data}\n{new_lens}')
    return new_lens


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


def write(df):  # 已完成
    file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/股票抽籤DATA/DATA.txt'
    with open(file_path, 'a', encoding='UTF-8') as file:
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

    time = soup.find_all('td', style="width:100px;")
    start_time, end_time = [], []
    for step in range(lens):
        start_time.append(time[step].text.strip().split('~')[0])
        end_time.append(time[step].text.strip().split('~')[1])

    # df = convert_pd(number, state)
    # # write(df)
    # new_lens = data_dup(number, state, lens)

    return number, state, lens, name, end_time, profit_reward


if __name__ == "__main__":
    url = 'https://histock.tw/stock/public.aspx'
    token = 'SFJszrFZMHievEBqql9GFFSU29PtoMdwgeEOH84CX6c'
    data = get(url)
    df = convert_pd(*data[:2])
    # write(df)
    new_lens = data_dup(*data[:3])
    resp = notify(*data, new_lens)
