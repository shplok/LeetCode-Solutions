class Solution:
    def findLucky(self, arr: List[int]) -> int:

        freq = {}
        max_luck = -1
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num in freq:
            if num == freq[num]:
                max_luck = max(max_luck, num)

        return max_luck
