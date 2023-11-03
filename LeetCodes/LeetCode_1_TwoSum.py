# 給一個裡面元素為int的陣列，陣列中會有兩個元素加起來等於target，回傳這兩個元素的位置。
# 範例：
# [2, 7, 11, 15], target = 9，2+7=9，因此回傳[1,2]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    ans = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):  # i+1避免重複運算
            if nums[i]+nums[j] == target:
                ans.extend([nums[i], nums[j]])
                break
    print(ans)
