class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        cnt = 1
        pre = 0
        res = 0

        for left in range(1, len(nums)):
            if nums[left] > nums[left-1]:
                cnt += 1
            else:
                pre, cnt, = cnt, 1
            res = max(res, min(pre, cnt))
            res = max(res, cnt // 2)
        return res
