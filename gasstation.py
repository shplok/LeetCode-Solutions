class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total_tank = 0
        curr_tank = 0
        start = 0
        for i in range(len(cost)):
            
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1