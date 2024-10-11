class Solution:
    def isHappy(self, n: int) -> bool:  
        while n >= 10:
            sums = 0
            digits = [int(digit) for digit in str(n)]
            for num in range(len(digits)):
                sums += (digits[num])**2
            n = sums
        if n == 1 or n == 7:
            return True
        return False