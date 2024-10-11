class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maj = len(nums) // 2
        freqMap = {}

        for num in nums:
            if num in freqMap:
                freqMap[num] += 1      
   
            else:
                freqMap[num] = 1

            if freqMap[num] > maj:
                return num        
    
    