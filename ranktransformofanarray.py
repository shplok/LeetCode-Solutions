class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        temp = sorted(set(arr))

        for i in range(len(temp)):
           # in sorted arr (temp), rank arr[i] = temp[i + 1]
           rank[temp[i]] = i+1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]   

        return arr