class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * length
        # list of len length init to 1
        for i in range(1, length):
            products[i] = products[i-1] * nums[i-1]
        
        right = nums[-1]
        for i in range(length-2, -1, -1):
            products[i] *= right
            right *= nums[i]

        return products
            
            