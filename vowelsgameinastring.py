class Solution:
    def doesAliceWin(self, s: str) -> bool:
        if not s:
            return False
        # optimal move for alice if vowel num is odd, take all and win
        # optimal move for alice if vowel num is even, take all but 1
        vowels = 'aeiou'
        cnt = 0

        for char in s:
            if char in vowels:
                cnt += 1

        return False if cnt == 0 else True
