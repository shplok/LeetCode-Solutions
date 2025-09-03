class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # string s -> len m
        # string t -> len n

        # return -> minimum window substring of s
        # such that, every char in string t (including duplicates) are in the window.
        # most likely a dynamic sliding window with dictionary
    
        tFreqs = {}
        windowFreqs = {}

        for char in t:
            if char in tFreqs:
                tFreqs[char] += 1
            else:
                tFreqs[char] = 1

        left = 0
        required = len(tFreqs)
        formed = 0
        min_len = float('inf')
        best_l, best_r = None, None

        for right in range(len(s)):

            windowFreqs[s[right]] = windowFreqs.get(s[right], 0) + 1
            if s[right] in tFreqs and windowFreqs[s[right]] == tFreqs[s[right]]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best_l, best_r = left, right

                
                left_char = s[left]
                windowFreqs[left_char] -= 1
                
                if left_char in tFreqs and windowFreqs[left_char] < tFreqs[left_char]:
                    formed -= 1

                left += 1


        if best_l is not None:
            return s[best_l:best_r+1]
        return ""
