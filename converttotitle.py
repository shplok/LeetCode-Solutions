class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        colOut = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            col = columnNumber % 26

            columnNumber //= 26
            colOut = chr(ord('A') + col) + colOut
        return colOut
