class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0 
        max_count = 0
        seen = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
            else:
                seen += 1

            while seen > 1:

                if nums[left] == 1:
                    count -= 1
                else:
                    seen -= 1
                
                left += 1
            
            max_count = max(max_count, count)
        return max_count if max_count != len(nums) else max_count - 1
        
