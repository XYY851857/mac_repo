import re
import time
import traceback
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from stock.股票抽籤LINE_Notify import report


def get(pack1):
    kp, lai, hou, url = pack1
    chrome_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
                              AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36', }
    html = requests.get(url, headers=chrome_headers)

    soup = BeautifulSoup(html.text, 'html.parser')
    data = soup.find_all('tr', class_="D(f) Fz(16px) Fz(14px)--sm767 Fz(12px)!--mbsm4 Lh(24px) Lh(20px)--sm767 Fw(400) C(#232a31) Bdbw(1px) Bdbs(s) Bdbc(#e0e4e9)")
    # print(data[0].text.strip().replace(',', '').split('票'))
    for step in range(0, len(data)):
        cache = re.split(r'[票市縣]', data[step].text.strip().replace(',', ''))
        # print(cache)
        # kp = int(cache[1])
        # lai = int(cache[2])
        # hou = int(cache[3])
        # print(f'kp:{kp}    lai:{lai}    hou:{hou}')
        kp += int(cache[1])
        lai += int(cache[2])
        hou += int(cache[3])
        # print(f'kp:{kp}    lai:{lai}    hou:{hou}')

        # kp = int(data[step].text.strip().replace(',', '').replace('票', ''))
        # print('kp', kp)
        # lai = int(data[step+1].text.strip().replace(',', '').replace('票', ''))
        # print('lai', lai)
        # hou = int(data[step+2].text.strip().replace(',', '').replace('票', ''))
        # print('hou', hou)
    return kp, lai, hou


def notify(data):
    kp, lai, hou = data
    url = "https://notify-api.line.me/api/notify"
    token = "O22XmpnxuecnSEFPJl01cKFQBhDMy7Omn1RMXjLwiiq"  # TEST Token
    headers = {"Authorization": "Bearer " + token}
    message = f'\n時間：{datetime.now().strftime("%Y-%m-%d    %H:%M:%S")}\n柯文哲/吳欣盈：{kp} 票\n賴清德/蕭美琴：{lai} 票\n侯友宜/趙少康：{hou} 票\n總票數：{kp + lai + hou} 票\n**票數僅供參考**'

    data = {"message": message}
    resp = requests.post(url, headers=headers, data=data)
    if str(resp) != '<Response [200]>':
        report(__file__, resp)
    return str(resp)



if __name__ == "__main__":
    while True:
        try:
            url = "https://tw.news.yahoo.com/election-2024/"
            kp = lai = hou = 0
            pack1 = (kp, lai, hou, url)
            data = get(pack1)
            resp = notify(data)
            break
            # time.sleep(60)
        except Exception as e:
            traceback.print_exc()
            print(e)
            # report(__file__, e)
            break
            # time.sleep(15)

