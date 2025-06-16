class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        j = 0
        if len(s) == 0 and len(t) == 0:
                return True  
         
        for i in range(len(t)):
              
            if s and t and s[j] == t[i]:
                j += 1
            
            if j == len(s):
                return True
            
        return False
