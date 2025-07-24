class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        #dp[i] = min num of coins needed to make i
        for i in range (1, amount+1):
            for c in coins:
                if i - c >= 0: # we can use c to contribute to i
                    dp[i] = min(dp[i], dp[i-c]+1) 
        return -1 if dp[amount] == float('inf') else dp[amount]
