class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)
        
        if k > 0:
            return [sum((code*2)[i+1:i+1+k]) for i in range(len(code))]
        else:
            return [sum((code*2)[i+len(code)-abs(k):i+len(code)]) for i in range(len(code))]