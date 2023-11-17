"""
nums給定一個長度為 的整數數組n和一個整數target，找到三個整數nums使得總和最接近target。
傳回三個整數的和。
您可以假設每個輸入都有一個解決方案。
範例1：
輸入： nums = [-1,2,1,-4], target = 1
輸出： 2
解釋：最接近目標的總和為 2。(-1 + 2 + 1 = 2)。
範例2：
輸入： nums = [0,0,0], target = 1
輸出： 0
解釋：最接近目標的總和為 0。(0 + 0 + 0 = 0)。
限制條件：
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


def algo(num_algo, target_algo):
    large = None
    for i in range(len(num_algo)):
        for j in range(i + 1, len(num_algo)):
            for k in range(j + 1, len(num_algo)):
                number = num_algo[i] + num_algo[j] + num_algo[k]
                ab_v = abs(target_algo - number)
                if large is None or ab_v < large:
                    large = number
    return large


if __name__ == "__main__":
    # num, target = [-1, 2, 1, -4], 1  # Example 1
    num, target = [0, 0, 0], 1  # Example 2
    ans = algo(num, target)
    print(ans)
