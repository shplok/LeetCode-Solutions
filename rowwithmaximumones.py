class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        resultRow = 0 
        maxOnes = 0     

        for i in range(len(mat)):
            
            oneCount = sum(mat[i])
            if oneCount > maxOnes:
                maxOnes = oneCount
                resultRow = i
        
        return [resultRow, maxOnes]

