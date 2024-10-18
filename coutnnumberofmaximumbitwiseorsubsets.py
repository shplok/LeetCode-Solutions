class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = 0

        for num in nums:
            maxOr |= num
        return self.countSubsets(nums, 0, 0, maxOr)
    
    def countSubsets(self, nums: List[int], index: int, currOr: int, targetOr: int) -> int:

        if index == len(nums):
            return 1 if currOr == targetOr else 0
            
        noCurr = self.countSubsets(nums, index + 1, currOr, targetOr)
        withCurr = self.countSubsets(nums, index + 1, currOr | nums[index], targetOr)

        return noCurr + withCurr