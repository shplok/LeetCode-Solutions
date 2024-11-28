class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # loop backwards from the end of array
        # find the first word encased by spaces
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
            elif s[i] == " " and count > 0: 
                break
        return count