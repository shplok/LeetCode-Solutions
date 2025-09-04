class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = 0
        max_same = "-9999"
        for i in range(1, len(num)-1):
            if num[i-1] == num[i] == num[i+1]:
                curr = num[i-1:i+2]
                if int(curr) > int(max_same):
                    max_same = curr

        return max_same if len(max_same) == 3 else "" 
