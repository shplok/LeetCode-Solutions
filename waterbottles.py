class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = 0
        while numBottles >= numExchange:
            N = numBottles // numExchange
            cnt += numExchange * N
            numBottles -= numExchange * N
       
            numBottles += N

        return cnt + numBottles
