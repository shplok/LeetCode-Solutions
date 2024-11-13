class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for left in range(n - 1):
            right_min = self.lower_bound(nums, left + 1, n - 1, lower - nums[left])
            right_max = self.upper_bound(nums, left + 1, n - 1, upper - nums[left])
            
            if right_min <= right_max:
                count += right_max - right_min + 1
        
        return count

    def lower_bound(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def upper_bound(self, nums, left, right, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right
