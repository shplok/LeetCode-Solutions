class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                count += 1
            if count >= 3:
                return True
            if arr[i] % 2 == 0 and count >= 0 and count < 3:
                count = 0
        return False
