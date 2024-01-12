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
    data = soup.find_all('td', class_="Bxz(bb) Px(24px) Px(4px)--md1019 Px(4px)--sm767 Py(12px) Ta(end) Fxb(0) Fxg(1) Fxs(1)")
    for step in range(0, len(data), 3):
        kp += int(data[step].text.strip().replace(',', ''))
        lai += int(data[step+1].text.strip().replace(',', ''))
        hou += int(data[step+2].text.strip().replace(',', ''))
    return kp, lai, hou


def notify(data):
    kp, lai, hou = data
    url = "https://notify-api.line.me/api/notify"
    token = "OUZVMu567J4aJTV3ttYCaA2pc7vlpqX86xeH7Emm3u1"
    headers = {"Authorization": "Bearer " + token}
    message = f'\n時間：{datetime.now().strftime("%Y-%m-%d    %H:%M:%S")}\n柯文哲/吳欣盈：{kp} 票\n賴清德/蕭美琴：{lai} 票\n侯友宜/趙少康：{hou} 票\n總票數：{kp + lai + hou} 票'

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
            time.sleep(30)
        except Exception as e:
            traceback.print_exc()
            print(e)
            report(__file__, e)
            time.sleep(15)

