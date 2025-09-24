class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        res = []

        if (numerator < 0 or denominator < 0) and not(numerator < 0 and denominator < 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))

        rem = numerator % denominator
        if rem == 0:
            return "".join(res)

        res.append('.')

        remMap = {}
        while rem != 0:
            if rem in remMap:
                idx = remMap[rem]
                res.insert(idx, "(")
                res.append(")")
                break

            remMap[rem] = len(res)
            rem *= 10
            res.append(str(rem // denominator))
            rem %= denominator

        return "".join(res)
         
