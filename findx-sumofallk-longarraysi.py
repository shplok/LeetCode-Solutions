class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        if k >= len(nums) + 1:
            return []
        ans = []

        def xSum(nums):
            res = 0
            freqs = {}
            for num in nums:
                freqs[num] = 1 + freqs.get(num,0)

            heap = []
            for i, j in freqs.items():
                heapq.heappush(heap, (j, i))
                if len(heap) > x:
                    heapq.heappop(heap)

            for i, j in heap:
                res += i * j
            return res

        for i in range(0,len(nums)-k+1):
            new = nums[i:k+i]
            if k == x:
                ans.append(sum(new))
            else:
                ans.append(xSum(new))

        return ans
