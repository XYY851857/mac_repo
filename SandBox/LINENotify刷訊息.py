import threading

import requests


def notify():
    url = "https://notify-api.line.me/api/notify"
    token = "p9w0gHpW8GMAdin0YSdpq467C73swBi9h8rjzdcM7nA"
    headers = {"Authorization": "Bearer " + token}
    message = '老師我有87426張創意，平均成本1450，不知道什麼時候停利比較好？'

    data = {"message": f"{message}"}
    resp = requests.post(url, headers=headers, data=data)
    return resp


if __name__ == "__main__":
    while True:
        thread1 = threading.Thread(target=notify)
        thread2 = threading.Thread(target=notify)
        thread3 = threading.Thread(target=notify)
        thread4 = threading.Thread(target=notify)
        thread5 = threading.Thread(target=notify)
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()


