class Solution:
    def reverse(self, x: int) -> int:
        
        neg =  x < 0
        x = abs(x)

        num = list(str(x))
        num.reverse()
        rev = int("".join(num))

        if neg:
            rev = -rev

        if rev > 2147483646 or rev < -2147483647: return 0
        return rev
        
