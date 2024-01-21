"""
判斷一個int整數是否是自己的迴文數，不能使用額外的空間來操作。
提示：
負整數會是自己的迴文數嗎(ex. -1)
如果你想用字串來解是不行的，因為不能使用額外的空間。
你也可以反轉整數，如果你之前已經做過LeetCode 7. Reverse Integer，你會知道反轉後的數可能會超過integer的最大值。
"""


def algo(value):
    if value == value[::-1]:
        return True
    return False


if __name__ == '__main__':
    data = str(input('input num : '))
    data = algo(data)
    if data:
        print('是')
    else:
        print('不是')
