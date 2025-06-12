class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in num:
                res.append(i)
        return res
        
