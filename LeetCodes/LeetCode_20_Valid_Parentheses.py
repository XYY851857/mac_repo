"""
給定一個字串s，只包含字元'('、')'、'{' 、'}'、'[' 和 ']'，判斷輸入字串是否有效。

輸入字串在以下情況下有效：
1. 左括號必須由相同類型的括號封閉。
2. 左括號必須以正確的順序關閉。
3. 每個右括號都有一個對應的相同類型的左括號。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "}", "{": "}", "<": ">"}
        closing_brackets = set(mapping.values())
        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or mapping[stack.pop()] != char:
                    return False

        return not stack


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{}"
    print(solution.isValid(s))
