class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # A = 1 -> AB = 28 -> A*26 + B(2) = 28
        # ZY = 26 * Z(26) + Y(25)
        # Essentially, for the length of columnTitle, all except the last index should be mult by 26
        # Last column should be added to final product

        prod = 0
        n = len(columnTitle)
        for i in range(n):
            if i != n-1:
                prod += ((ord(columnTitle[i].lower()) - ord('a')) + 1) * (26**(n-i-1))

            else:
                prod += ((ord(columnTitle[i].lower()) - ord('a')) + 1)
        return prod
