class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while 1:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        chaser = nums[0]
        while chaser != slow:
            slow = nums[slow]
            chaser = nums[chaser]


        return slow
       
