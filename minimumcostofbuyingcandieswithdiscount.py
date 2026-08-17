class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = sum(cost)
        sub = 0
        for i in range(0, len(cost)-2, 3):
            sub += cost[i+2]

        return total - sub

