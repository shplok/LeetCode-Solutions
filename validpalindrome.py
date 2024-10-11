class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(c for c in s if c.isalnum())
        word = word.lower()
        
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        
        return True