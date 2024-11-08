class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xorProd = 0
        ans = [0] * n
        for num in nums:
            xorProd = xorProd ^ num   
        mask = (1 << maximumBit) - 1

        for i in range(n):
            ans[i] = xorProd ^ mask
            xorProd = xorProd ^ nums[n - 1 - i]
        return ans