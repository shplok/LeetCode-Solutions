class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_held = 0

        while i < j:
            temp_lo = min(height[i], height[j]) # lowest point for water
            temp = temp_lo * (j - i) # low point times the width
            max_held = max(max_held, temp)

            if height[i] <= height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1

        return max_held
            
