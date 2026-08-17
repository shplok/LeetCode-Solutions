class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0

        if not nums:
            return 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
                    
        del nums[k+1:]           
        return k + 1
        
