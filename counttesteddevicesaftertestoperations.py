class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
        count = 0

        for battery in batteryPercentages:
            count += battery > count
            
        return count