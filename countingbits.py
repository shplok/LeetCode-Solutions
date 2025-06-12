class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = int(bin(i)[2:].count("1"))
            print(ans[i])
        return ans
      
