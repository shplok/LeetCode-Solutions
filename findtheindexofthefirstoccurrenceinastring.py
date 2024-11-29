class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:  # If needle is empty, return 0
            return 0
        
        needle_len = len(needle)
        haystack_len = len(haystack)
        
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        
        return -1