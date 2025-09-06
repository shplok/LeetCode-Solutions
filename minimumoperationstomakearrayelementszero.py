class Solution:
    def get(self, num: int) -> int:
        i = 1
        base = 1
        count = 0
        while base <= num:
            count += ((i+1) // 2) * (min(base * 2 - 1, num) - base + 1)
            i += 1
            base *= 2
        return count

    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for query in queries:
            res += (self.get(query[1]) - self.get(query[0] - 1) + 1) // 2
        return res
