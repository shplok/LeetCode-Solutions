class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return i of target if in nums else -1

        lo = 0
        hi = len(nums) - 1
        mid = -1
        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
                
        return -1
        
