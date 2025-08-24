class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # look for bounding coordinates that contain 1s
        min_col = float('inf')
        min_row = float('inf')

        max_col = 0
        max_row = 0     

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:

                    min_col = min(min_col, j)
                    min_row = min(min_row, i)
                    max_col = max(max_col, j)
                    max_row = max(max_row, i)           
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)
