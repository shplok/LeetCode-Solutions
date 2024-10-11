class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        Sn = (n * (n + 1) // 2)
        Sa = sum(nums)

        return (Sn - Sa)

                  