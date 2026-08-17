class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            factorCount = factorSum = 0
            i = 1
            while i * i <= num:
                if num % i == 0:
                    factorCount += 1
                    factorSum += i
                    if i * i != num:
                        factorCount += 1
                        factorSum += num // i
                i += 1
            if factorCount == 4:
                res += factorSum
        return res
