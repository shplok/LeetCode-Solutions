class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sortedSkill = sorted(skill)
        length = len(sortedSkill)
        targetSum = sortedSkill[0] + sortedSkill[length - 1]
        chemistry = 0

        i = 0
        j = length - 1
        while i < j:
            if sortedSkill[i] + sortedSkill[j] != targetSum:
                return -1
            
            chemistry += sortedSkill[i] * sortedSkill[j]
            i += 1
            j -= 1
    
        return chemistry

            
        