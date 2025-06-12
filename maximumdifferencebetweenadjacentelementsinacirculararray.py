class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxDifference = 0 
        
        for i in range(1, len(nums)):
            
            m1 = abs(max(nums[i], nums[i-1]) - min(nums[i], nums[i-1]))
            maxDifference = m1 if m1 > maxDifference else maxDifference  

        m1 = abs(max(nums[len(nums)-1], nums[0]) - min(nums[len(nums)-1], nums[0]))    
        maxDifference = m1 if m1 > maxDifference else maxDifference

        return maxDifference

        #------ Less Memory -------#
        # nums.append(nums[0])
        # return max(abs(nums[i] - nums[i+1]) for i in range(len(nums)-1)) 
            
