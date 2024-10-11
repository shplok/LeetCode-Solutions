class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return median(sorted(nums1 + nums2)) <-- one-liner in nlogn 

        len1 = len(nums1)
        len2 = len(nums2)

        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        left = (len1 + len2 + 1) // 2
        lo = 0
        hi = len1

        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = left - mid1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

             # Determine values of l1, l2, r1, and r2
            if mid1 < len1:
                r1 = nums1[mid1]
            if mid2 < len2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                
                if (len1 + len2) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
            
                hi = mid1 - 1
            else:
                
                lo = mid1 + 1
        
        return 