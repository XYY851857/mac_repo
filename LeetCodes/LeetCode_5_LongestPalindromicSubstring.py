"""
給定一個字串s，傳回最長的 回文的子字串在s.
範例1：
輸入： s = "babad"
輸出： "bab"
解釋： "aba" 也是有效答案。
範例2：
輸入： s = "cbbd"
輸出： "bb"
限制條件：
1 <= s.length <= 1000
s僅由數字和英文字母組成。
"""


class Solution:
    def __init__(self, s):
        self.s = s

    def algo(self):
        data = []
        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s)):
                if self.s[i] == self.s[j]:
                    data.append(''.join(self.s[i: j + 1]))
        return data


if __name__ == "__main__":
    s = 'snfoawneiofnaw'
    solution = Solution(s)
    ans = solution.algo()
    print(ans)
