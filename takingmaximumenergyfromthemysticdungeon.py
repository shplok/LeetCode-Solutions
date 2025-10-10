class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        dp = energy[:]
        for i in range(len(energy)-1, -1, -1):
            if i + k < len(energy):
                dp[i] += dp[i+k]

        return max(dp)
