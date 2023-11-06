def algo(list1):
    i = 0
    lens = len(list1)
    #list1[-1] = (int(list1[-1])+1)

    while i < lens:
        if list1[0] == "2":
            list1.insert(0, "0")
        if list1[-(i + 1)] == "2":
            list1[-(i + 1)] = "0"
            list1[-(i + 2)] = str(int(list1[-(i + 2)]) + 1)
        i += 1
    return list1


if __name__ == "__main__":
    num = int(input("請輸入一個數字："))
    list1 = [str(digit) for digit in str(num)]
    ans = algo(list1)
    ans = [str(digit) for digit in ans]  # 轉換元素為字元字串
    print("結果:", ''.join(ans))

