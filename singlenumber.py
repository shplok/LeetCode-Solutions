class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        solo = 0
        if len(nums) == 1: return nums[0]
        else:
            for i in range(len(nums)):
                
                solo ^= nums[i]
        return solo
        
