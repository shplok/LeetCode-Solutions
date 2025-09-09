class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # delay is the number of days until secret is shared
        # forget is how many days after learning to forgert
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = sum(dp[j] for j in range(max(1, i - forget + 1), i - delay + 1))

        
        return sum(dp[j] for j in range(max(1, n - forget + 1), n + 1)) % (10**9 + 7)
