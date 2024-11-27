class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False] * len(nums)
        dp[-1] = True
        length = len(nums)

        for i in range(length - 2, -1, -1):
            farthest = min(i + nums[i], length - 1)
            for j in range(i + 1, farthest + 1):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]
            