class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        res = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                res += i
                if i != num // i:
                    res += num // i
        return res == num
