class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in numSet:
                count = 0
                while(num + count) in numSet:
                    count += 1
                longest = count if count >= longest else longest
        return longest

            