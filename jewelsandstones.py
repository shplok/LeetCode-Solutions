class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        freqMap = {}

        for stone in stones:
            if stone in jewels:
                if stone in freqMap:
                    freqMap[stone] += 1
                else :
                    freqMap[stone] = 1
        
        return sum(freqMap.values())