class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
          
        dist1 = abs(z - abs(x))
        dist2 = abs(z - abs(y))

        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            return 0
            
