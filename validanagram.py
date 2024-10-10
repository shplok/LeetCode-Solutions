class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        countS, countT = {}, {}
        # this is how you create hashmaps in python

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False              
        return True
            # the 1 + count is bascially incrementing the prev count by 1 every time you see the char
            # in python you can use .get for hashmaps with 0 as the initial value

            # if you wanted to do with a space complexity of constant do this 
            # return sorted(s) == sorted(t)