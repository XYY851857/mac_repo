"""
給一個陣列跟一個數字，移除陣列中所有跟數字相同的元素。
不可以使用另外的陣列來處理，全部的操作都要在同一個陣列中。
陣列中的元素可以隨意排序。
範例：
nums = [3, 1, 2, 3, 2]， val = 3
應該要return 陣列的長度3，因為裡面的3被移除後剩[1,2,2].
"""


def algo(data):
    data.sort()
    return data


if __name__ == "__main__":
    nums = [3, 1, 2, 3, 2]
    val = 3
    new_data = algo(nums)
    print(new_data[:val])
