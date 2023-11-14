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
    solution_instance = Solution(s)
    ans = solution_instance.algo()
    print(ans)
