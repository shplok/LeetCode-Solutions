class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        preMap = {}
            
        for num in arr1:
            strNum = str(num)
            prefix = ""
            for char in strNum:
                prefix += char
                preMap[prefix] = preMap.get(prefix, 0) + 1
            
        maxLen = 0

        for num in arr2:
            strNum = str(num)
            prefix = ""
            for char in strNum:
                prefix += char
                if prefix in preMap:
                    maxLen = max(maxLen, len(prefix))

        return maxLen