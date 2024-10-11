class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 4 or n == 1:
            return True

        if n != 4 and n < 8:
            return False

        return self.isPowerOfFour(n / 4)
        