class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == divisor:
            return 1

        res = 0
        divid = abs(dividend)
        divis = abs(divisor)

        while (divid >= divis):
            count = 0
            while (divid >= (divis << (count+1))):
                count += 1
            divid -= divis << count
            res += 1 << count

        if (dividend < 0) ^ (divisor < 0):
            res = -res

        return res
