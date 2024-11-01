class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[0]
        prev = s[0]
        freq = 1

        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                prev = s[i]
                freq = 1
            if freq < 3:
                res += s[i]
        return res
        