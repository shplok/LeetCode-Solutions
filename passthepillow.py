class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        currPos = 1
        currTime = 0
        direction = 1

        while currTime < time:
            if 0 < currPos + direction <= n:
                currPos += direction
                currTime += 1
            
            else:
                direction *= -1
        return currPos