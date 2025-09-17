class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algo
        best = float('-inf')
        curr = 0

        for x in nums:
            curr = max(x, curr + x)
            best = max(best, curr)
        return best
        
