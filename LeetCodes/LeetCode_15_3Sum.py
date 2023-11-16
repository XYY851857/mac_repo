"""
[nums[i], nums[j], nums[k]]給定一個整數數組 nums，傳回所有滿足i != j、i != k、 、 、j != k和的三元組nums[i] + nums[j] + nums[k] == 0。
請注意，解決方案集不得包含重複的三元組。
範例1：
輸入： nums = [-1,0,1,2,-1,-4]
輸出： [[-1,-1,2],[-1,0,1]]
解釋：
nums[0] + nums [1] + nums[2] = (-1) + 0 + 1 = 0。nums
[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.nums
[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0。
不同的三元組是 [-1,0,1] 和 [-1,-1,2]。
請注意，輸出的順序和三元組的順序並不重要。
範例2：
輸入： nums = [0,1,1]
輸出： []
解釋：唯一可能的三元組總和不為 0。
範例3：
輸入： nums = [0,0,0]
輸出： [[0,0,0]]
解釋：唯一可能的三元組總和為 0。
"""


def algo(num):
    ans1 = []
    for i in range(0, len(num)):
        for j in range(i + 1, len(num)):
            for k in range(j + 1, len(num)):
                if num[i] != num[j] and num[i] != num[k] and num[j] != num[k]:
                    if (num[i] + num[j] + num[k]) == 0:
                        ans1.append([num[i], num[j], num[k]])
                        # return ans1 如果只要求一組
    return ans1


if __name__ == "__main__":
    num = [-1, 0, 1, 2, -1, -4]
    ans = algo(num)
    print(ans)
