class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        if k == 1:
            return True

        inc = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + 1
            else:
                inc[i] = 1

        for j in range(k, len(nums)):
            if inc[j-k] >= k and inc[j] >= k:
                return True
        return False
