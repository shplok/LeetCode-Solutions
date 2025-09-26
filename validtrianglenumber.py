class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        cnt = 0
        nums.sort()
        
        for c in range(2, len(nums)):
            left, right = 0, c-1
            while left < right:
                if nums[left] + nums[right] > nums[c]:
                    cnt += (right - left)
                    right -= 1
                else:
                    left += 1
            
        return cnt
        
