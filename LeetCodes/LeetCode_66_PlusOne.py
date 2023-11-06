"""
[十進位換算]
給一包含非數整數的陣列，其中每一個值代表該位數的值，對這個陣列加1。
範例：
19 = [1,9] ， 19+1 = 20 = [2,0]。
"""


def algo(list1):
    i = 0
    list1[-1] += 1
    if list1[0] == 9:
        list1.insert(0, 0)
    while i < len(list1):
        if list1[-(i + 1)] == 10:
            list1[-(i + 2)] += 1
            list1[-(i + 1)] = 0
        i += 1
    return list1


if __name__ == "__main__":
    """
    num = int(input("input : "))
    list1 = [int(digit) for digit in str(num)]
    """
    list1 = [9, 9, 9]
    ans = algo(list1)
    print(ans)

