class Solution:
    def minimumChairs(self, s: str) -> int:
        
        count = 0
        maxPeople = 0
        for i in range(len(s)):
            if s[i] == "E":
                count += 1
                maxPeople = max(count, maxPeople)
            else:
                count -= 1

        return maxPeople
