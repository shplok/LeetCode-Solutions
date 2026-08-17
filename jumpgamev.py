class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # arr = arry full of ints with index i
        # can jump from i to i+x iff < len(arr) / i-x iff i-x >= 0
        # KEY LOGIC: can only jump from one index to the next if arr[i] > arr[j] and arr[i] > arr[k] for k between i and j
        

        # store memoization dict and check first if an element at that index has content, if so return that
        # init count to 0
        # sample current idx, for all elements in the array lt arr[i] (forwards and backwards) and 

        # maxJumps = max(count, maxJumps)

        memo = {}
        maxCount = 0

        def max_jumps_from(i):
            if i in memo:
                return memo[i]

            best = 1
            #left
            for l in range(i-1, max(-1, i-d-1), -1):
                if arr[l] >= arr[i]:
                    break
                best = max(best, 1 + max_jumps_from(l))

            #right
            for r in range(i+1, min(i+d+1, len(arr))):
                if arr[r] >= arr[i]:
                    break
                best = max(best, 1 + max_jumps_from(r))

            memo[i] = best
            return memo[i]
            
        for i in range(len(arr)):
            maxCount = max(maxCount, max_jumps_from(i))
            
        return maxCount
