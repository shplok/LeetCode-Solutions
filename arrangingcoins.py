class Solution:
    def arrangeCoins(self, n: int) -> int:
        totalRows =  1

        while n >= totalRows:
            n -= totalRows
            totalRows += 1
        return totalRows - 1
