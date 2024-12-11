class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tot = 0
        for i in range(len(nums)):
            if len(nums) % (i+1) == 0:
                tot += nums[i]**2

        return tot