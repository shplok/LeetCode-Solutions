class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        maxLen = 0
        for i in range(len(s)):
            if s[i] in longest:
                # rem characters before including the repeated char
                longest = longest[longest.index(s[i]) + 1:]
            longest += s[i]
            maxLen = max(maxLen , len(longest))
        return maxLen
        