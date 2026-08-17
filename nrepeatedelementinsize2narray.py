class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # freqs = {}
        # target = len(nums) // 2
        # for num in nums:
        #     if num not in freqs:
        #         freqs[num] = 1
        #     else:
        #         freqs[num] += 1

        #     if freqs[num] == target:
        #         return num
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
