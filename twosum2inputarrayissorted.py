class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        sum1 = 0

        
        while l < r:
            sum1 = numbers[l] + numbers[r]
            if sum1 == target:
                return [l+1, r+1]
            elif sum1 > target:
                r -= 1
            else:
                l += 1


    