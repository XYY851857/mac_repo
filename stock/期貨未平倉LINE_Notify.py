"""
url : "https://tw.stock.yahoo.com/future/futures_uncovered.html"
"""
import pandas as pd
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


def notify(data_set, time):
    dealer, investment_trust, foreign_investment = data_set
    url = "https://notify-api.line.me/api/notify"
    # token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    token = "p9w0gHpW8GMAdin0YSdpq467C73swBi9h8rjzdcM7nA"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    message = f'\n資料擷取時間：{time}\n外資{foreign_investment}\n投信{investment_trust}\n自營商{dealer}'

    data = {"message": message}
    resp = requests.post(url, headers=headers, data=data)
    return resp


def convert_pd(data):
    dealer, investment_trust, foreign_investment = data

    result_df = []
    # print(data)
    df_data = pd.DataFrame({
        'foreign': foreign_investment,
        'invest': investment_trust,
        'dealer': dealer
    }, index=['0'])
    result_df.append(df_data)
    combined_df = pd.concat(result_df)
    # print(combined_df)

    return combined_df


def write(new_list):  # 已完成
    df = convert_pd(new_list)
    file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/期貨未平倉DATA/DATA.txt'
    with open(file_path, 'w', encoding='UTF-8') as file:
        df.to_csv(file, index=False)


def data_dup(data):
    dealer_get, invest_get, foreign_get = data
    file_df = pd.read_csv('/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/期貨未平倉DATA/DATA.txt', encoding='utf-8')
    foreign = file_df['foreign'][0:len(file_df) + 1].tolist()
    invest = file_df['invest'][0:len(file_df) + 1].tolist()
    dealer = file_df['dealer'][0:len(file_df) + 1].tolist()
    for step in range(0, len(file_df)):
        if foreign[step] == foreign_get and invest[step] == invest_get and dealer[step] == dealer_get:
            # 判斷資料是否已在資料庫
            return False  # 重複
        else:
            return True  # 不重複


if __name__ == "__main__":
    url = "https://www.taifex.com.tw/cht/3/futContractsDate"
    time = (datetime.now()).strftime("%Y/%m/%d")
    data_set = get(url)
    write(data_set)
    if data_dup(data_set):
        resp = notify(data_set, time)
        if resp:
            write(data_set)
