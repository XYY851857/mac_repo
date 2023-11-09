"""
這題目敘述有點長，我記得以前這是以前堂哥跟我玩的(猜數字遊戲)[http://codepen.io/skyyen999/full/VedwqQ/]，上面那一大串英文的意思是，這邊有一串隱藏的號碼(secret number)，然後你朋友會猜一串號碼， 如果號碼數字與位置都對了，給一個bull，數字對但位置不對，給一個cow。
範例:
Secret number:  "1807"
Friend's guess: "7810"
上面範例可以發現8得到一個bull，剩下1,0,7得到一個cow，所以得到1A3B
Secret number:  "1123"
Friend's guess: "0111"
第二個範例，第二個1得到一個bull，Friend's guess 第三個1得到一個cow(比對secret number的第一個1)，因此得到1A1B
"""
import random as r


def algo(guess, secret_num):
    guess = list(guess)
    secret_num = list(secret_num)
    count_a, count_b = 0, 0
    for item in range(guess):
        if guess[item] == secret_num[item]:
            count_a += 1



if __name__ == '__main__':
    while True:
        secret_num = r.randint(1, 9999)
        guess = int(input('請輸入1～9999數字 ： '))
        report = algo(guess, secret_num)
