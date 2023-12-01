class Solution:
    def letterCombinations(self, digit_input):
        num_dict = {'1': [], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
                    '0': [' '], }

        def backtrack(index, path):
            if index == len(digits):
                combinations.append("".join(path))
                return

            current_digit = digits[index]

            if current_digit == '1':
                backtrack(index + 1, path)
            if current_digit in num_dict and num_dict[current_digit] is not None:
                for char in num_dict[current_digit]:
                    path.append(char)
                    backtrack(index + 1, path)
                    path.pop()

        combinations = []
        backtrack(0, [])
        return combinations


if __name__ == "__main__":
    solution = Solution()
    digits = input("input digit:")
    ans = solution.letterCombinations(digits)
    print(ans)
