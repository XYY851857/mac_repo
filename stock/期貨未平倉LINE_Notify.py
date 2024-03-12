"""
url : "https://tw.stock.yahoo.com/future/futures_uncovered.html"
"""
import os.path
import traceback
import pandas as pd
# -*- coding: utf-8 -*-
import requests
import pymongo
from bs4 import BeautifulSoup
from datetime import datetime



def report(file_name, e):
    url = "https://notify-api.line.me/api/notify"
    token = "O22XmpnxuecnSEFPJl01cKFQBhDMy7Omn1RMXjLwiiq"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    data = {"message": f"\n{datetime.now().strftime("%Y-%m-%d    %H:%M:%S")}\n{file_name}:\n{e}"}
    requests.post(url, headers=headers, data=data)


def clean_strip(text):
    return ''.join(text.split())


def get(url):
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                          AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    num = soup.find_all('font', color='blue')
    dealer = int(clean_strip(num[5].text).replace(',', ''))
    invest = int(clean_strip(num[11].text).replace(',', ''))
    foreign = int(clean_strip(num[17].text).replace(',', ''))

    return dealer, invest, foreign
-1522, 18, -681

def notify(data_set, time, db_data):
    dealer, invest, foreign = data_set
    foreign_db, invest_db, dealer_db = db_data
    url = "https://notify-api.line.me/api/notify"
    token = "DEd00NVq4jTeZZ8yfMMP1OoOoCkZyhy1wTq4wEWmGjG"
    # token = "tXTEUdyi4ULLp7HX7C8x6Tw6Kpwq0VIJJNywp1kX4CK"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    message = f'\n資料擷取時間：{time}\n外資    :{foreign:>6} ({foreign - foreign_db})\n投信    :{invest:>6} ({invest - invest_db})\n自營商:{dealer:>6} ({dealer - dealer_db})'

    data = {"message": message}
    resp = requests.post(url, headers=headers, data=data)
    if str(resp) != '<Response [200]>':
        report(__file__, resp)
    return str(resp)


def convert_pd(data):
    dealer, investment_trust, foreign_investment = data

    result_df = []
    df_data = pd.DataFrame({
        'foreign': str(foreign_investment),
        'invest': str(investment_trust),
        'dealer': str(dealer)
    }, index=['0'])
    result_df.append(df_data)
    combined_df = pd.concat(result_df)

    return combined_df


def write(new_list):  # 已完成
    df = convert_pd(new_list)  # pandas轉換

    collections = client['open_interest']['DATA']
    data_dict = df.to_dict(orient='records')  # 轉換字典結構
    collections.drop()  # 初始化資料集
    collections.insert_many(data_dict)  # 寫入


def data_dup(data):
    global db_data
    dealer_get, invest_get, foreign_get = data
    collections = client["open_interest"]["DATA"]
    file_data = collections.find()
    file_df = pd.DataFrame(list(file_data))
    foreign = file_df['foreign'][0]
    invest = file_df['invest'][0]
    dealer = file_df['dealer'][0]
    db_data = [int(foreign), int(invest), int(dealer)]

    if str(foreign) == str(foreign_get) and str(invest) == str(invest_get) and str(dealer) == str(dealer_get):
        # 資料必須轉字串，否則不到三位數資料為int
        # 判斷資料是否已在資料庫
        print(f'{datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}: Duplicate')
        return False  # 重複
    else:
        return True  # 不重複


if __name__ == "__main__":
    url = "https://www.taifex.com.tw/cht/3/futContractsDate"
    global client
    global db_data
    db_data = []
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    try:
        time = (datetime.now()).strftime("%Y/%m/%d")
        data_set = get(url)
        if data_dup(data_set):
            resp = notify(data_set, time, db_data)
            if str(resp) == '<Response [200]>':  # 傳送成功寫入資料庫
                write(data_set)
                print(f'{os.path.basename(__file__)}  {datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}:  {resp}')
        client.close()
    except Exception as e:
        traceback.print_exc()
        report(__file__, traceback.format_exc())  # 回報主控台錯誤訊息內容，會觸發Notify，請小心使用
        client.close()
