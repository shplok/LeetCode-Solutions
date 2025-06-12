class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # correct but too slow
        # for i in range(n):
        #     if 2**i == n:
        #         return True

        # return False
        # 2^1 = 2 = 10 
        # n = 4 = 2^2 = 100 10 & 100 -> 0
        # n = 3 = 011 = 11 & 10 = 10
        # n = 5 = 101 = 10 & 101 = 0
        return True if n & (n-1) == 0 and n > 0 else False
