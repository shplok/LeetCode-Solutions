class Solution:
    def canWinNim(self, n: int) -> bool:
        #  n of 1-3 -> true regardless
        #  n = 4, me, you, me, you* me me me, you* me, me, you, you* -> false
        #  n = 5-7 -> can take stones to make it 4 for the opponent -> true
        #  n = 8 cant take stones to make it 4, opponent can make it 4 -> false
        if n in [1, 2, 3]: return True
        else:
            return n % 4 != 0
        
