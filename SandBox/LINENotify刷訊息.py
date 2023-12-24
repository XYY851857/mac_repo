import threading
import random

import requests


def notify():
    url = "https://notify-api.line.me/api/notify"
    token = "38UlHhkykIWI1844mAgl73IfbVHkACFPAIcuaRm85oe"
    headers = {"Authorization": "Bearer " + token}
    message = '欸嘿'

    data = {"message": f"{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


if __name__ == "__main__":
    while True:
        threads = []
        num = random.randint(15, 20)
        # 創建和啟動線程
        for _ in range(num):
            thread = threading.Thread(target=notify)
            thread.start()
            threads.append(thread)

        # 等待所有線程完成
        for thread in threads:
            thread.join()