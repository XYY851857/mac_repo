"""
給一個整數，找出這個整數有幾個'1'，
例如11用32-bit表示 '00000000000000000000000000001011'，
總共有3個1，
return 3
"""


def algo(num1):
    count = 0
    while num1 != 0:
        count += num1 & 1
        num1 >>= 1
    return count


if __name__ == "__main__":
    num1 = int(input("input: "))
    ans = algo(num1)
    print(ans)
