class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        charset = set(word)
        count = 0
        for ch in charset:
            if ch.lower() == ch:
                if ch.upper() in charset:
                    count += 1
        return count
        