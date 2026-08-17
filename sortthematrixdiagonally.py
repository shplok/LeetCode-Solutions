'''
make a hashmap 
key is i-j
value is a list of all elements on the diagonal
sort that list and then reconstruct
'''
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        matMap = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j not in matMap:
                    matMap[i-j] = [mat[i][j]]
                else:
                    matMap[i-j].append(mat[i][j])
        
        for diag in matMap.values():
            diag.sort(reverse=True)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = matMap[i-j].pop()
                
        return mat
                
