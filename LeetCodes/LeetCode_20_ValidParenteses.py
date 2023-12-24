class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"(": ")", "[": "]", "{": "}", "<": ">"}
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
