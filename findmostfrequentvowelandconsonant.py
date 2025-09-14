class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowelFreq = {}
        consFreq = {}
        vowels = 'aeiou'

        for char in s:
            if char in vowels:
                if char not in vowelFreq:
                    vowelFreq[char] = 1
                else:
                    vowelFreq[char] += 1
            else:
                if char not in consFreq:
                    consFreq[char] = 1
                else:
                    consFreq[char] += 1

        if not consFreq:
            return max(vowelFreq.values())
        elif not vowelFreq:
            return max(consFreq.values())

        return max(consFreq.values()) + max(vowelFreq.values())
        
