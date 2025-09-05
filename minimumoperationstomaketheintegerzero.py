class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        i = 1
        while 1:
            x = num1 - num2 * i
            if x < i:
                return -1
            if i >= x.bit_count():
                return i
            i += 1  
            
