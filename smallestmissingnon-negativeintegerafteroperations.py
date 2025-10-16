class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mex = 0
        m = Counter(i % value for i in nums)
        while m[mex % value] > 0:
            m[mex % value] -= 1
            mex += 1

        return mex
        
