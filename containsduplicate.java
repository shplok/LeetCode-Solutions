class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

        
        # a nested for loop would have a time complexity of n^2 and space complexity of constant which  is not efficient

        # remember that a hashset is highly efficient when working through problems like this