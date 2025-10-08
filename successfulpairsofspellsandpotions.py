class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        i = 0

        for i in range(len(spells)):
            lo = 0
            hi = len(potions) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if spells[i] * potions[mid] < success:
                    lo = mid + 1
                else:
                    hi = mid - 1
            res.append(len(potions) - lo)
            
        return res
        
