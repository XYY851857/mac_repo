"""
給兩個已經排序過的的整數陣列nums1與nums2，將nums2合併入nums1之中
注意：
nums1會有有足夠的空間可以塞入兩個陣列(nums1.length = m+n)，m為nums1的元素數量，n為nums2的元素數量
範例： nums1 = [1,1,2,4,6,null,null,null], m = 5, nums2 = [2,3,7], n = 3
合併後 nums1 = [1,1,2,2,3,4,6,7]
"""


def algo(nums1, nums2):
    data = nums1 + nums2
    data = sorted(data)
    return data


if __name__ == '__main__':
    nums1 = [1, 1, 2, 4, 6]
    nums2 = [2, 3, 7]
    ans = algo(nums1, nums2)
    print(ans)