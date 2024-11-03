class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return True if len(s) == len(goal) and (s+s).find(goal) != -1 else False

