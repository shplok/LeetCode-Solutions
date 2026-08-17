'''
given:
text of arbitrary characters
we can ONLY swap 2 characters

returns:
len of longest substring
'''

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        freqMap = {}
        for char in text:
            freqMap[char] = freqMap.get(char, 0) + 1
                
        maxLen = 0
        i = 0
        j = 0
        window = {}

        while j < len(text):
            window[text[j]] = window.get(text[j], 0) + 1
            j += 1
            
            maxChar = max(window.values()) if window else 0

            while (j - i) - maxChar > 1:
                window[text[i]] -= 1
                if window[text[i]] == 0:
                    del window[text[i]]
                i += 1
                maxChar = max(window.values()) if window else 0

            currChar = max(window, key=window.get) if window else ''

            if (j - i) > maxChar:
                possible = min(j - i, freqMap.get(currChar, 0))
            else:
                possible = min(j - i + 1, freqMap.get(currChar, 0))

            maxLen = max(possible, maxLen)

        return maxLen
