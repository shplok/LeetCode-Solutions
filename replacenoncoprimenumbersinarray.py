class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            curr = num
            while stack:
                g = gcd(stack[-1], curr)
                if g == 1:
                    break
                curr = stack.pop() * curr // g  # LCM
            stack.append(curr)
        
        return stack
