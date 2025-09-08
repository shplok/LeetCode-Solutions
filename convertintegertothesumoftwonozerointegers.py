class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        res = []

        for i in range(1, n):
            a = i
            b = n - i

            if '0' not in str(a) and '0' not in str(b):
                res.append(a)
                res.append(b)
                break
        return res
