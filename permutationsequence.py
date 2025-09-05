class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        k -= 1 # to get 0-indexed
        def factorial(num):
            if num == 0 or num == 1:
                return 1
            return num * factorial(num-1)
        perm = ""
        digits = [i for i in range(1, n+1)]

        index = k // factorial(n-1)
        perm += str(digits[index])
        digits.pop(index)
        k %= factorial(n-1)

        while digits:
            factor = factorial(len(digits)-1)
            index = k // factor
            perm += str(digits[index])
            del(digits[index])
            k %= factor

        return perm
