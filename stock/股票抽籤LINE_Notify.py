"""
url = 'https://histock.tw/stock/public.aspx'
截止日/價差/市場別/中籤率
名稱/
"""
import traceback
import os.path
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import pymongo


def report(file_name, e):
    url = "https://notify-api.line.me/api/notify"
    token = "O22XmpnxuecnSEFPJl01cKFQBhDMy7Omn1RMXjLwiiq"  # TEST token
    headers = {"Authorization": "Bearer " + token}
    data = {"message": f"\n{datetime.now().strftime("%Y-%m-%d    %H:%M:%S")}\n{file_name}:\n{e}"}
    requests.post(url, headers=headers, data=data)


def merge_list(data):
    number, state, new_lens, name, end_time, profit_reward, price, amount, rate = data
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
        # token = "tXTEUdyi4ULLp7HX7C8x6Tw6Kpwq0VIJJNywp1kX4CK"  # TEST token
        token = "7ABygdMg7ZHO9B55ysAYlAJk28ZLJyHxdgJJJW1buIG"
        headers = {"Authorization": "Bearer " + token}
        data = {
            "message": f'\n資料時間：{datetime.now().date()}\n{message}\n\n**此為自動推播**\n**請以公告為主**\n**價差僅供參考**'}
        resp = requests.post(url, headers=headers, data=data)
        if str(resp) != '<Response [200]>':
            report(__file__, resp)
        return resp

    if lens == 0:  # 無新資料
        return False
    else:
        new_list = merge_list(data)
        message = f'\n\n'.join([' '.join(row) for row in new_list])
        resp_sent = sent(message)
        return resp_sent


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

    collections = pymongo.MongoClient("mongodb://localhost:27017/")["draw_lots"]["DATA"]
    data_dict = df.to_dict(orient='records')

    collections.update_one({},{"$set": {"$each": data_dict}}, upsert=True)

    # file_path = '/Users/xyy/PycharmProjects/LeetCode_MAC/DATA/股票抽籤DATA/DATA.txt'
    # with open(file_path, 'w', encoding='UTF-8') as file:
    #     df.to_csv(file, index=False)


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

    name_data = soup.find_all('td', style="color:#5482AB;font-weight:bold;width:120px;")
    # print(name_data)
    name, number = [], []
    for step in range(0, lens):
        number.append(name_data[step].text.split('\xa0')[0].strip())
        name.append(name_data[step].text.split('\xa0')[1].strip())

    market_type_data = soup.find_all('td', style="width:70px;")
    market_type = []
    for step in range(0, lens):
        market_type.append(market_type_data[step].text.strip())

    profit_target = soup.find_all('td', style="font-weight:bold;width:67px;")
    # print(profit_target)
    profit_reward, profit_percent = [], []
    for step in range(0, lens * 3, 3):
        profit_reward.append(profit_target[step].text.strip())
        profit_percent.append(profit_target[step + 1].text.strip())
        # print(profit_target[step].text.strip())  # 價差
        # print(profit_target[step+1].text.strip())  # 報酬率
    # for step in range(0, lens * 2, 2):  # 遇到初上市/櫃會有bug
    #     profit1, profit2 = profit_data[step].text.strip(), profit_data[step + 1].text.strip()
    #     profit_reward.append(profit1)
    #     profit_percent.append(profit2)

    time_data = soup.find_all('td', style="width:100px;")
    start_time, end_time = [], []
    for step in range(0, lens):
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
    try:
        data = get(url)  # 取得資料
        resp = notify(data)
        if str(resp) == '<Response [200]>':  # 傳送成功寫入資料庫
            # write(*data[:2])
            print(f'{os.path.basename(__file__)}  {datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}:  {resp}')
    except Exception as e:
        traceback.print_exc()
        report(__file__, traceback.format_exc())  # 回報主控台錯誤訊息內容，會觸發Notify，請小心使用
