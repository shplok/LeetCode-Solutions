class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if n < 3:
            return 0
        for i in range(n-1, 1, -1):
            if nums[i] < (nums[i - 2] + nums[i - 1]):
                return (nums[i - 2] + nums[i - 1] + nums[i])

        return 0