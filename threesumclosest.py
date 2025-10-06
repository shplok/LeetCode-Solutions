class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float('inf')
        nums.sort()

        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                curr = nums[i] + nums[l] + nums[r]

                if abs(curr - target) < abs(closest - target):
                    closest = curr

                if curr < target: l += 1
                elif curr > target: r -= 1
                else:
                    return curr

        return closest
