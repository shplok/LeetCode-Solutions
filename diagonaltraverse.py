class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        res = []
        diags = {}

        for i in range(rows):
            for j in range(cols):
                if i+j not in diags:
                    diags[i+j] = []
                diags[i+j].append(mat[i][j])


        for k in range(len(diags)):
            if k % 2 == 0:
                res.extend(diags[k][::-1])
            else:
                res.extend(diags[k])

        return res
