class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        if n == 3:
            return values[0] * values[1] * values[2]
        
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):          
            for i in range(n - length):     
                j = i + length              
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], 
                        dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])

        return dp[0][n-1]
        
