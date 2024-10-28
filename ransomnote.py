# SOLUTION 1

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, "", 1)
        return True

# SOLUTION 2

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charMap = {}
        for char in magazine:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
                
        for char in ransomNote:
            if char not in charMap or charMap[char] == 0:
                return False
            charMap[char] -= 1
        return True