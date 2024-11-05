class Solution:
    def minChanges(self, s: str) -> int:
        currLen = 0
        currChar = s[0]
        minChanges = 0

        for char in s:
            if char == currChar:
                currLen += 1
                continue
            if currLen % 2 == 0:
                currLen = 1
            else:
                currLen = 0
                minChanges += 1
    
            currChar = char
        return minChanges