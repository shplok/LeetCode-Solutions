class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        length = len(s)

        allpossible = {}

        for char in s:
            if char in allpossible:
                allpossible[char] += 1
            else:
                allpossible[char] = 1

        if letter in allpossible:
            freq = allpossible[letter]
        else:
            return 0
        
        return freq * 100 // length
