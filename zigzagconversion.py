class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        down = False
        curr_row = 0

        for char in s:
            rows[curr_row] += char

            if curr_row == 0 or curr_row == numRows - 1:
                down = not down

            curr_row += 1 if down else -1
        return "".join(rows)                
        