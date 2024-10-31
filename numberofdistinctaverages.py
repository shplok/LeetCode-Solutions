class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        while len(nums) > 0:
            tMin = min(nums)
            tMax = max(nums)
            nums.remove(tMin)
            nums.remove(tMax)

            avg.add((tMin + tMax)/2)
        return len(avg)