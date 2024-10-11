class Solution:
    def numSquares(self, n: int) -> int:
        squares = [0] * (n + 1)

        for i in range(1, n + 1):
            squares[i] = float('inf')
        
            for j in range(1, int(math.sqrt(i)) + 1):
                squares[i] = min(squares[i], 1 + squares[i - j*j])

        return squares[n]