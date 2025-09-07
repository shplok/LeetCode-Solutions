class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # nums with odd digits are never symmetric
        # sum of first half == sum of second half of nums

        count = 0
        for i in range(low, high+1):
            length = len(str(i))
            if length % 2 == 0:
                if sum(int(n) for n in str(i)[length//2:]) == sum(int(n) for n in str(i)[:length//2]):
                    count += 1
        return count
