class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        else:
            res = []
            for i in range(numRows):
                row = [1] * (i+1)
                for j in range(1, i):
                    row[j] = res[i-1][j-1] + res[i-1][j]
                res.append(row)
                   
            return res
                    
