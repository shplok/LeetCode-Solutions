class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter

        nums.sort()
        counts = Counter(nums)

        maxFreq = 0
        start = 0
        end = 0
        n = len(nums)

        # iterate through every possible target value
        for element in range(nums[0], nums[-1] + 1):
            # expand right boundary to include numbers within [element - k, element + k]
            while end < n and nums[end] <= element + k:
                end += 1

            # shrink left boundary to exclude numbers < element - k
            while start < n and nums[start] < element - k:
                start += 1

            window_size = end - start
            max_bound = counts[element] + numOperations
            freq = min(window_size, max_bound)

            maxFreq = max(maxFreq, freq)

        return maxFreq
