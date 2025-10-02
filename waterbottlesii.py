class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        def switch(i: int, j: int):
            if i < j:
                return 0
            return 1 + switch(i-j+1, j+1)

        return numBottles + switch(numBottles, numExchange)
        
