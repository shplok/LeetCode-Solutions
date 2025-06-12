class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        lst = nums1 if len(nums1) < len(nums2) else nums2
        for num in lst:
            if num in nums1 and num in nums2:
                res.add(num)

        return list(res)
