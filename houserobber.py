class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return max(nums)
        else:
            dp = []
            dp.append(nums[0])
            dp.append(max(nums[0], nums[1]))
            for i in range(2, len(nums)):
                dp.append(max((dp[i-2] + nums[i]), dp[i-1]))

            return max(dp)
