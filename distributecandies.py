class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candyMap = {}

        for candy in candyType:
            if candy in candyMap:
                candyMap[candy] += 1
            else:
                candyMap[candy] = 1

        return min(len(candyMap), len(candyType) // 2)
        