"""
反轉一個int整數。
x = 123 , return 321 x = -123 , return -321
提示：
假如10，100反轉後會長怎樣。
你有注意到反轉後的數可能會超過Integer的範圍嗎，例如說1000000003反轉後就超過了32-bit的integer。這種情況要怎麼處理?
在這個問題中，超過integer只要回傳0就可以。
"""


def abc(value):
    if value[-1] == '-':
        value.insert(0, value.pop())
    return value


if __name__ == "__main__":
    x, y = 123, -1234456

    x_list = list(str(x))
    y_list = list(str(y))

    x_list.reverse()
    y_list.reverse()
    x_list = "".join(abc(x_list))
    y_list = "".join(abc(y_list))
    print(x_list)
    print(y_list)
