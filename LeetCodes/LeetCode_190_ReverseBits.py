"""
給一個32 bits的int整數，反轉整數的bits。
範例： 整數43261596 轉換成bits = 00000010100101000001111010011100，將bit反轉00111001011110000010100101000000再轉成整數964176192回傳
進階：如果這個function會被呼叫很多次，要怎麼做最佳化?
"""


def algo(num_algo):
    bits = 0
    for _ in range(32):
        bits = (bits << 1) | (num_algo & 1)
        num_algo >>= 1

    return bits


if __name__ == '__main__':
    num1 = 43261596
    num2 = algo(num1)
    print(num2)
