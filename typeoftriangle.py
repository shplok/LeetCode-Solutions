class Solution:    
    def triangleType(self, nums: List[int]) -> str:
        def switch_ex(n):
            if n == 1: 
                return "equilateral"
            if n == 2: 
                return "isosceles"
            if n == 3: 
                return "scalene"
            
        freqMap = {}
        if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:
            
            for num in nums:
                if num in freqMap:
                    freqMap[num] += 1
                else:
                    freqMap[num] = 1
            return switch_ex(len(freqMap))
        return "none"
