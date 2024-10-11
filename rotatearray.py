class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # reverse all elements. k is the pivot, at index nums[k], 
        # reverse first k elements and then reverse last len-k -> len elements 
        pivot = (len(nums) - k) % len(nums)
        nums[:] = nums[pivot:] + nums[:pivot]
        return nums
