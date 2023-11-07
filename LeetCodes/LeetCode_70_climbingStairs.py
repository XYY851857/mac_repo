"""
你正在爬一個階梯。到頂端總共需走n階。
每次你都可以選擇爬1階或2階，問有幾種不同的方法可以爬到階梯頂端
"""


def algo(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2

    count1 = 1
    count2 = 2
    for i in range(3, n+1):
        current = count1 + count2
        count1, count2 = count2, current
    return count2


if __name__ == "__main__":
    n = int(input('請輸入階層 : '))
    ans = algo(n)
    print(ans)
