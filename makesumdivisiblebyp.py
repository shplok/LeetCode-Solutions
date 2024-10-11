class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        allSum = sum(nums)
        remainder = allSum % p

        if remainder == 0:
            return  0
        prefixSums = {0: -1}
        currSum = 0
        minLen = len(nums)

        for i, num in enumerate(nums):
            currSum += num
            currRemainder = currSum % p
            requiredModVal = (currRemainder - remainder) % p

            if requiredModVal in prefixSums:
                minLen = min(minLen, i - prefixSums[requiredModVal])

            prefixSums[currRemainder] = i

        return minLen if minLen < len(nums) else -1