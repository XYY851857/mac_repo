"""
給一個排序過的陣列，移除重複的值，每個元素只能留下一個。
不能使用其他的陣列空間，必需在本來的陣列中操作。
範例： [1,1,2] 去除重複的1之後，剩下[1,2]，回傳陣列的長度2。
"""


def algo(data):
    data = list(set(data))  # 使用集合去除重複資料，在轉換回串列
    return data


if __name__ == "__main__":
    list1 = [1, 2, 1, 3, 5, 2, 1]
    ans = algo(list1)
    print(ans)
