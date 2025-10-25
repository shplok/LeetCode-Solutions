class Solution:
    def totalMoney(self, n: int) -> int:
        
        total = 0
        week = 1

        while n > 0:
            for i in range(min(n, 7)):
                total += week + i
            
            n -= 7
            week += 1
        return total
