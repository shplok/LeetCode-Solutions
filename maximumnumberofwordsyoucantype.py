class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        count = len(words)
        for word in words:
            if any(ch in word for ch in brokenLetters):
                count -= 1

        return count
