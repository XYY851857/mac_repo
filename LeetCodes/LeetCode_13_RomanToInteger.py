"""
給一個羅馬數字符號，將之轉為整數，這個數字一定落在1 到 3999 之間。
範例：
I = 1, IX = 9
"""
def trans(data):
    global roman_to_int
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    arr = [roman_to_int[char] for char in data.upper()]  # 分隔並轉換為大寫
    return arr



def algo(arr):
    sum1 = 0
    if len(arr) == 1:
        sum1 += arr[0]
        return sum1

    for i in range(len(arr)):
        if not arr:
            break
        elif len(arr) == 1 or arr[0] is max(arr):
            sum1 += arr[0]
            arr.pop(0)
        elif arr[0] >= arr[1]:
            sum1 += arr[0] + arr[1]
            arr = arr[2:]
        elif arr[0] <= arr[1]:
            sum1 += arr[1] - arr[0]
            arr = arr[2:]
    return sum1


if __name__ == '__main__':
    num = input('input: ')
    data = trans(num)
    ans = algo(data)
    print(f'ans: {ans}')
