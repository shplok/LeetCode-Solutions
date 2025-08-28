class Solution:
    def mySqrt(self, x: int) -> int:
    

        if x < 2:
            return x

        l = 0
        r = x // 2
        
        while l <= r:
            m = (l+r) // 2
            m_sq = m * m

            if m_sq == x:
                return m
            
            elif m_sq < x:
                l = m+1
            else:
                r = m-1
        return r
