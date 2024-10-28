class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        longest = -1
        numSet = set(nums)

        for num in sortedNums:
            count = 0
            curr = num
            while curr in numSet:
                numSet.remove(curr)
                curr = curr ** 2
                count += 1

            longest = max(longest, count)

        return longest if longest > 1 else -1