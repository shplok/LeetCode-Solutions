class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        mismatches = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatches.append(i)
        
        if len(mismatches) == 2:
            i = mismatches[0]
            j = mismatches[1]
            
            return s[i] == goal[j] and s[j] == goal[i]
        
        return False
                
