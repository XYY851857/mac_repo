"""
給定一個整數nums數組n，傳回所有唯一四元組的數組 [nums[a], nums[b], nums[c], nums[d]]，使得：
0 <= a, b, c, d < n
a、b、c和d是不同的。
nums[a] + nums[b] + nums[c] + nums[d] == target
您可以按任何順序返回答案。
範例1：
輸入： nums = [1,0,-1,0,-2,2]，目標 = 0
輸出： [[-2,-1,1,2],[-2,0,0,2],[ -1,0,0,1]]
範例2：
輸入： nums = [2,2,2,2,2]，目標 = 8
輸出： [[2,2,2,2]]
"""


def algo(nums, target):
    result = []
    nums.sort()
    for one in range(0, len(nums) - 3):
        for two in range(one + 1, len(nums) - 2):
            for three in range(two + 1, len(nums) - 1):
                for four in range(three + 1, len(nums)):
                    data = nums[one] + nums[two] + nums[three] + nums[four]
                    if data == target:
                        result.append([nums[one], nums[two], nums[three], nums[four]])
    return result


if __name__ == "__main__":
    nums = [2, 2, 2, 2, 2]
    target = 8
    ans = algo(nums, target)
    print(ans)