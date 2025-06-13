class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        # def qsort(arr):
        #     if len(arr) <= 1:
        #         return arr
        #     else:
        #         pivot = arr[0]
        #         lt = [x for x in arr[1:] if x < pivot]
        #         eq = [x for x in arr[1:] if x == pivot]
        #         gt = [x for x in arr [1:] if x > pivot]
        #         return qsort(lt) + [pivot] + eq + qsort(gt)
        # nums = qsort(nums)
        if nums != sorted(nums):
            nums.sort()

        def canformpairs(d):
            count = 0
            i = 0
            while i < len(nums) - 1:
                
                if nums[i+1] - nums[i] <= d:
                    count += 1
                    i += 2
                else:
                    i += 1
                if count >= p:
                    return True
            return False

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            mid = (lo+hi) // 2
            if canformpairs(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
                
