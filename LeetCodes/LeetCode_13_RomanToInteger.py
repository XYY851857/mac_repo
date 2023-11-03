"""
給一個羅馬數字符號，將之轉為整數，這個數字一定落在1 到 3999 之間。
範例：
I = 1, IX = 9
"""


def trans(data):
    arr = [char for char in data]  # 分隔
    for item in range(len(arr)):
        if arr[item] == "I" or arr[item] == "i":
            arr[item] = int(1)
        elif arr[item] == "V" or arr[item] == "v":
            arr[item] = int(5)
        elif arr[item] == "X" or arr[item] == "x":
            arr[item] = int(10)
        elif arr[item] == "L" or arr[item] == "l":
            arr[item] = int(50)
        elif arr[item] == "C" or arr[item] == "c":
            arr[item] = int(100)
        elif arr[item] == "D" or arr[item] == "d":
            arr[item] = int(500)
        elif arr[item] == "M" or arr[item] == "m":
            arr[item] = int(1000)
    return arr


"""
From ChatGPT
使用字典來映射羅馬數字符號和整數值
def trans(data):
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    arr = [roman_to_int[char] for char in data.upper()]  # 分隔並轉換為大寫
    return arr
"""


def algo(arr):
    if arr[0] >= arr[-1] != 1:
        print(arr[-2])
        ex = arr[-1] - arr[-2]
        print('HELLO')
        arr.pop()
        arr.pop()
        arr.append(ex)
        print(arr)

    for i in range(len(arr) - 1):
        if arr[0] >= arr[1]:
            num_algo = arr[0] + arr[1]
            arr.insert(0, num_algo)
            print('row{1} :{0}'.format(arr, i + 1))
            arr.pop(1)
            print('row{1} :{0}'.format(arr, i + 1))
            arr.pop(1)
        elif arr[0] <= arr[1]:
            num_algo = arr[1] - arr[0]
            arr.pop(i)
            arr.insert(0, num_algo)
            arr.pop(i + 1)
    print('return :{}'.format(arr))
    return arr


if __name__ == '__main__':
    while True:
        num = input('input: ')
        data = trans(num)
        ans = algo(data)
        print('ans: {}'.format(int(ans[0])))
