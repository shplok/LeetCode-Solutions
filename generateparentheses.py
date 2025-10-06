class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = [] 
        def backtrack(curr, opened, closed):
            
            if len(curr) == 2 * n:
                res.append(curr)

            if opened < n:
                backtrack(curr + '(', opened+1, closed)
            if closed < opened:
                backtrack(curr + ')', opened, closed+1)

        backtrack("", 0, 0)
        return res
            
