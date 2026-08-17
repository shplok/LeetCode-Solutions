def helper(start1, length1, start2, length2):
    res1 = float('inf')
    res2 = float('inf')

    for i in range(len(start1)):
        res1 = min(res1, start1[i] + length1[i])
    for i in range(len(start2)):
        res2 = min(res2, max(start2[i], res1) + length2[i])

    return res2   

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        land_water = helper(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = helper(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(land_water, water_land)
