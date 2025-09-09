class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s) == 1:
            return 1

        freqs = {}
        count = 0
        for i in range(len(s)):
            if s[i] not in freqs:
                freqs[s[i]] = 1
            else:
                freqs[s[i]] += 1


        for char in freqs:
            if freqs[char] % 2 == 0:
                count += freqs[char]
            else:
                count += (freqs[char] - 1)      

        if any(freqs[char] % 2 == 1 for char in freqs):
            count += 1

        return count
  
