class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()           

        begin = strs[0]
        end = strs[-1]
        min_len = min(len(begin), len(end))
        i = 0
        
        while i < min_len and begin[i] == end[i]:
    
            i += 1
        
        return begin[:i]
        