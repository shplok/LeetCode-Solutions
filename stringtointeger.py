class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        while i < len(s) and s[i] == " ":
            i += 1

        neg = False
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            neg = (s[i] == '-')
            i += 1

        res = []
        while i < len(s) and s[i].isdigit():
            res.append(s[i])
            i += 1

        if not res:
            return 0

        num = int("".join(res))
        if neg:
            num = -num

        if num < -2**31:
            return -2**31
        if num > 2**31-1:
            return 2**31-1
        return num
      
