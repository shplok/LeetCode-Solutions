class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
            
        chars = {'2':'abc', '3':'def', 
                '4':'ghi', '5':'jkl', '6':'mno', 
                '7':'pqrs', '8':'tuv', '9':'wxyz'}
        digs = [dig for dig in digits]
        res = [""]
        for dig in digits:
            letters = chars[dig]
            new = []
            for combo in res:
                for letter in letters:
                    new.append(combo + letter)
            res = new
        
        return res      
                
