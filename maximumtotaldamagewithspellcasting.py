class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        
        if not power:
            return 0

        cnt = Counter(power)
        dmg = {j: j * cnt[j] for j in cnt}
        spells = [0, 0, 0] + sorted(list(dmg.keys()))
        n = len(spells)
        dp = [0] * n

        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + dmg[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + dmg[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + dmg[spells[i]])

        return dp[-1]
        
