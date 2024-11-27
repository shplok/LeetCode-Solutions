class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jump_pow = 0

        for n in nums:
            if jump_pow < 0:
                return False
            elif n > jump_pow:
                jump_pow = n
            jump_pow -= 1
        return True