class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
        max_diag = 0
        max_area = 0
        return_area = False

        for i in range(len(dimensions)):
            curr_diag = (dimensions[i][0] * dimensions[i][0]) + (dimensions[i][1] * dimensions[i][1])
            curr_area = dimensions[i][0] * dimensions[i][1]

            if curr_diag > max_diag:
                max_diag = curr_diag
                max_area = curr_area
            elif curr_diag == max_diag:
                max_area = max(max_area, curr_area)
            
            
        return max_area
