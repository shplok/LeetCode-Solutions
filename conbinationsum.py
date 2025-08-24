class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []

        def backtrack(start: int, target: int, curr: list[int]) -> None:
            if target == 0:
                out.append(curr[:])
                return
            
            if target < 0:
                return # overshot target

            for i in range(start, len(candidates)):
                curr.append(candidates[i])

                backtrack(i, target - candidates[i], curr)
                curr.pop()

        backtrack(0, target, [])
        return out 
