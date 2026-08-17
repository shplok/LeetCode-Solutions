class Solution:
    def maxDifference(self, s: str) -> int:
        # freqMap = {}
        # maxOdd = 0
        # minEven = 0
        # for c in s:
        #     if c not in freqMap:
        #         freqMap[c] = 1
        #     else:
        #         freqMap[c] += 1

        # for freq in freqMap.values():      
        #     if freq % 2 == 0:
        #         minEven = min(minEven, freq)
        #     elif freq % 2 == 1:
        #         maxOdd = max(maxOdd, freq)
                        

        # return maxOdd - minEven

        c = Counter(s)
        maxOdd = max(val for val in c.values() if val % 2 == 1)
        minEven = min(val for val in c.values() if val % 2 == 0)
        return maxOdd - minEven
