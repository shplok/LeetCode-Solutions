class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freqs = {}
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        
        cnt = 0

        for freq in freqs.values():
            cnt = max(cnt, freq)

        ultFreq = 0

        for freq in freqs.values():
            if freq == cnt:
                ultFreq += 1
        
        return ultFreq * cnt
