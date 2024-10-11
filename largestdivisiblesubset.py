class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums.sort()

        best = [1] * length
        parent = [-1] * length
        # if parent[i] == -1 then there is no parent 

        for i in range(length):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if best[j] + 1 > best[i]:
                        best[i] = best[j] + 1
                        parent[i] = j

        bestIndex = 0
        for i in range(length):
            if best[i] > best[bestIndex]:
                bestIndex = i

        answer = []
        while bestIndex != -1:
            # meaining while the best index has a parent
            answer.append(nums[bestIndex])
            bestIndex = parent[bestIndex]
        answer.reverse()
        return answer
        