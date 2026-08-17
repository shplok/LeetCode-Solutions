from collections import Counter

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0:
            return False

        freq = Counter(nums)
        groups = n // k

        return max(freq.values()) <= groups
