class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for num in range(len(nums)):
            
            if nums[num] != val:
                k += 1
                
            else: 
                nums[num] = -9994555


        while -9994555 in nums:
            nums.remove(-9994555)
        
        nums.sort()    

        return k         
