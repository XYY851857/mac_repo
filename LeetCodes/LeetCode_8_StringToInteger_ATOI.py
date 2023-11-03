"""
實作atoi將字串轉成int。
提示：小心仔細的考慮所有可能的輸入，如果你想挑戰自己，不要看下面的文字，直接想可能的輸入有哪些就可以開始寫了。
注意：這題目的輸入值有各種組合，你要先收集任何可能的輸入。
atoi的需求：
首先輸入的開頭可能是一連串的空白，因此要先找到第一個非空白字元。然後從這個字元開始可能會有正負號在數字的前面，將這些字串轉換成數字。
如果在數字後面有出現其他非數字的符號，因為他們對值沒有影響，可以忽略這些符號。
如果第一個非空白字元不是一個合法的int整數，或者字串裡面都是空白字元，那也視為不合法的輸入。
不合法的輸入回傳0，如果轉換後的數字num > INT_MAX (2147483647) 回傳2147483647， num < INT_MIN (-2147483648) 回傳 -2147483648
"""
int_max = 2147483647  # int最大值
int_min = -2147483647
data = 0


def trans(value):
    if not value.lstrip('-').isdigit():
        return 0
    value = int(value)
    if value > int_max:
        value = int_max
    elif value < int_min:
        value = int_min

    return value


if __name__ == '__main__':
    data = input('請輸入: ').strip()
    data = trans(data)
    print(data)
        # print(type(data))
