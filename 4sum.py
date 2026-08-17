class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # CONDITIONS
        # 0 <= a, b, c, d, < n
        # a, b, c, d -> distinct
        # nums[a] + nums[b] + nums[c] + nums[d] == target
        
#       res = []
        n = len(nums)
#         nums = sorted(nums)
        
#         for a in range(n):
#             for b in range(a+1, n):
#                 for c in range(b+1, n):
#                     for d in range(c+1, n):
#                         if nums[a] + nums[b] + nums[c] + nums[d] == target:
#                             if [nums[a], nums[b] ,nums[c], nums[d]] not in res:
#                                 res.append([nums[a], nums[b] ,nums[c], nums[d]])
#         return res
        nums.sort()
        res = []
        for a in range(n-3):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n-2):
                c = b+1
                d = n-1
                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total == target and [nums[a], nums[b], nums[c], nums[d]] not in res:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif total < target:
                        c += 1
                    else: 
                        d -= 1
        return res
