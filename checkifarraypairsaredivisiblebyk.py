class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
    
        n = len(arr) # Even length
        freqDict = {} 

        for i in arr:
            remainder = ((i % k) + k) % k
            if remainder in freqDict:
                freqDict[remainder] += 1
            else:
                freqDict[remainder] = 1

        for j in range(k):

                if j == 0:
                    if freqDict.get(j, 0) % 2 != 0:
                        return False
                elif j == k-j:
                    if freqDict.get(j, 0) % 2 != 0:
                        return False
                else:
                    if freqDict.get(j, 0) != freqDict.get(k-j, 0):
                        return False
                   
        return True