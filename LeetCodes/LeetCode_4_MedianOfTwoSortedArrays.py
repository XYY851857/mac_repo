"""
給定兩個已排序數組nums1和 ，nums2其大小分別為m和n，傳回兩個已排序數組的中位數。
整體運轉時間複雜度應為O(log (m+n)).
範例1：
輸入： nums1 = [1,3], nums2 = [2]
輸出： 2.00000
解釋：合併陣列 = [1,2,3]，中位數為 2。
範例2：
輸入： nums1 = [1,2], nums2 = [3,4]
輸出： 2.50000
解釋：合併陣列 = [1,2,3,4]，中位數為 (2 + 3) / 2 = 2.5。
"""


def algo(num1, num2):
    nums = list(set(num1 + num2))
    print(nums)
    lens = len(nums)
    if lens % 2 == 1:
        return nums[lens // 2]
    else:
        return (nums[lens // 2] + nums[lens // 2 - 1]) / 2


if __name__ == "__main__":
    num1, num2 = [1, 2, 3, 8], [4, 5, 6, 7]
    ans = algo(num1, num2)
    print("{:.1f}".format(ans))
