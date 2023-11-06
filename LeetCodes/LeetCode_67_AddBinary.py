"""
給兩個字元字串，回傳他們的總和(以字元字串回傳)。
範例：
a = '11'
b = '1' return '100'
"""


def algo(list1):
    i = 0
    list1[-1] = int(list1[-1]+1)
    if list1[0] == "2":
        list1[0] = "0"
        list1.insert(0, "0")
    while i < len(list1):
        if list1[-(i + 1)] == "2":
            list1[-(i + 2)] = str(int(list1[-(i + 2)]) + 1)
            list1[-(i + 1)] = "0"
        i += 1
    return list1


if __name__ == "__main__":
    num = int(input("input : "))
    list1 = [int(digit) for digit in str(num)]
    ans = algo(list1)
    print(ans)