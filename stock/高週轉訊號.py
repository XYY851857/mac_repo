import shutil

import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re
import os
from stock.turnover_rate_LINE_Notify import get


# def reset():
#     folder_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA'
#     for file in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file)
#         try:
#             if os.path.isfile(file_path):
#                 os.unlink(file_path)
#             elif os.path.isdir(file_path):
#                 shutil.rmtree(file_path)
#         except Exception as e:
#             print(f"Failed to delete {file_path}. Reason: {e}")
#     print('Initialized....')


def get_list():
    ori_data, time = get()
    process_data = [item[0].split("  ")[0] for item in ori_data[2:12]]
    for i in range(0, 9):
        if len(process_data[i]) != 4:
            process_data.pop(i)
    return process_data


def strategy(stock_id, df):  # 未完成
    count = 0
    while count <= 5:
        for item in range(len(df)):
            print(df.iloc[item, 4])
            var = df.iloc[item, 4]
            if count == 0:
                count += 1
            pass


def write(stock_id, df):
    folder_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA'
    file_name = f'{stock_id}_cache.txt'
    file_path = os.path.join(folder_path, file_name)
    os.makedirs(folder_path, exist_ok=True)
    with open(file_path, 'a', encoding='UTF-8') as file:
        df.to_csv(file, header=False)


def get_price(url, stock_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/111.25 (KHTML, like Gecko) Chrome/99.0.2345.81 Safari/123.36'}
    result_df = pd.DataFrame()
    print('connecting.....')
    for i in range(0, 2300):
        current, yday = None, None
        res = requests.get(url, headers=headers)
        # 最新價格
        current = [l for l in res.text.split('{') if len(l) >= 60][-1]
        current = current.replace('"', '').split(',')
        # 昨日價格
        yday = float(re.search(':.*', [l for l in res.text.split('{') if len(l) >= 60][-2].split(',')[4]).group()[1:])
        open_price = float(re.search(':.*', current[1]).group()[1:])
        high = float(re.search(':.*', current[2]).group()[1:])
        low = float(re.search(':.*', current[3]).group()[1:])
        close = float(re.search(':.*', current[4]).group()[1:])
        volume = float(re.search(':.*', current[5].replace('}]', '')).group()[1:])
        pct = round((float(re.search(':.*', current[4]).group()[1:]) / yday - 1) * 100, 2)
        df = pd.DataFrame({
            'open': open_price,
            'high': high,
            'low': low,
            'close': close,
            'volume': volume,
            'pct': pct
        }, index=[stock_id])
        result_df = pd.concat([result_df, df], ignore_index=True)
        time.sleep(1)
        print(df)
        write(stock_id, df)
        # strategy(stock_id, result_df)
    print(result_df)


if __name__ == "__main__":
    # reset()
    high_turn_list = get_list()
    for item in range(0, 1):
        stock_id = '2329'  # f'{high_turn_list[item]}'
        url = f"https://tw.quote.finance.yahoo.net/quote/q?type=ta&perd=d&mkt=10&sym={stock_id}&v=1&callback=jQuery111302872649618000682_1649814120914&_=1649814120915"
        get_price(url, stock_id)
