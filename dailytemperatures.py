class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res[i] == # of days after ith day to get warmer temp than res[i]
        # two pointer?
        
#         res = [0] * len(temperatures)
#         i = 0
#         j = 1
#         while j < len(temperatures):
#             if temperatures[j] > temperatures[i] and j-1 == 1:
#                 res[i] = j - i
#                 i = j
#                 j += 1
#             elif temperatures[j] > temperatures[i] and j-1 != 1:
#                 res[i] = j - i
#                 i += 1
#                 j = i + 1
#             else:
#                 j += 1
            
#         return res
        # stack
        res = [0] * len(temperatures)
        stack = [] # for indecies
        for i in range(len(temperatures)):
            while stack and temperatures[i] >  temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)
        return res
