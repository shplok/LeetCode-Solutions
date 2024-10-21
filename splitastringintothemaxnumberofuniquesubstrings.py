class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        maxCount = [0]
        self.backtrack(s, 0, seen, 0, maxCount)
        return maxCount[0]

    def backtrack(self, s: str, start: int, seen: set, count: int, maxCount: list) -> None:
        if count + (len(s) - start) <= maxCount[0]:
            return
        if start == len(s):
            maxCount[0] = max(maxCount[0], count)
            return
        for end in range(start + 1, len(s) + 1):
            subString = s[start:end]
            if subString not in seen:
                seen.add(subString)
                self.backtrack(s, end, seen, count + 1, maxCount)
                seen.remove(subString)
        return