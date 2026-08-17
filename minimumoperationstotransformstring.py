class Solution:
    def minOperations(self, s: str) -> int:
        if not s:
            return 0

        max_dist = 0

        for char in s:
            if char != 'a':
                dist = (ord('a') - ord(char)) % 26
                max_dist = max(max_dist, dist)
        return max_dist

        
