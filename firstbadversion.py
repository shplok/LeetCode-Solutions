# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # if mid is bad, then check left half, otherwise check right half
        def binSearch(lo, hi):
            
            while lo < hi: 
                mid = (lo + hi) // 2
                
                if isBadVersion(mid):
                    return binSearch(lo, mid)
                else:
                    return binSearch(mid+1, hi)
            return lo

        return binSearch(0, n)
   
