"""
給一個只包含'(', ')', '{', '}', '[' , ']'這些括號字元的字串，判斷這些括號是不是合法的。
右括號必須依照正確的順序出現，"()" 與 "()[]{}" 都是合法的，
但"(]" 和 "([)]"就不是。
"""


def algo(data):
    dict = {"(": ")", "[": "}", "{": "}", "<": ">"}
    stack = []

    for char in data:
        if char in dict.keys():
            stack.append(char)
        elif char in dict.values():
            if not stack or dict[stack.pop()] != char:
                return False
    return len(stack) == 0


if __name__ == '__main__':
    list = str(input("input: "))
    ans = algo(list)
    print(ans)

