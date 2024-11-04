class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        n = len(word)
        
        while i < n:
            char = word[i]
            count = 0
            while i < n and word[i] == char:
                count += 1
                i += 1
            while count > 0:
                comp += str(min(count, 9)) + char
                count -= 9
        return comp
