class Solution:
    def trap(self, height: List[int]) -> int:

        totalFill = 0
        left = 0
        right = len(height) - 1

        maxLeft = height[left]
        maxRight = height[right]


        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                if height[left] < maxLeft:
                    totalFill += maxLeft - height[left]
                
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                if height[right] < maxRight:    
                    totalFill += maxRight - height[right]
            

        return totalFill