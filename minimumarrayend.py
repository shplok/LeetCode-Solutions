class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x

        while n > 1:
            res = (res + 1) | x
            n -= 1
        return res
    
    # time limit exceeded as above code runs in O(n)


    # below is O(log n) solution

    class Solution:
        def minEnd(self, n: int, x: int) -> int:
            res = x
            n -= 1
            mask = 1

            while n > 0:
                if (mask & x) == 0:
                    res |= (n & 1) * mask
                    n >>= 1
                mask <<= 1
            return res
