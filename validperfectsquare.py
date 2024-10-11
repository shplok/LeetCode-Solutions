class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo = 2
        hi = num/2

        if num == 1:
            return True

        while hi >= lo:
            mid = (hi + lo) // 2


            if (mid * mid) == num:
                return True

            elif (mid * mid < num) and ((mid + 1) * (mid + 1)) > num:
                return False 

            elif (mid * mid) > num:
                hi = mid - 1
             
            else:
                lo = mid + 1
                
    
        return False
        