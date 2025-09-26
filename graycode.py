class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = []
        for i in range(0, 1<<n):
            gray.append(i^(i>>1))

        return gray
