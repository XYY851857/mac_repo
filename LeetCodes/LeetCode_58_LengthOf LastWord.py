"""
給一個字串s，其中包含大小寫字母與空白' '，回傳最後一個單字的長度，如果沒有最後一個單字，回傳0。
注意：單字的定義是由一串連續中間沒空白的字元所組成。
範例： Given s = "Hello World"，最後一個單字為world，長度為5。
"""


def algo(data):
    data = data.split()
    last_word = data[-1]
    return len(last_word)


if __name__ == "__main__":
    str1 = "Hello World"
    ans = algo(str1)
    print(ans)
