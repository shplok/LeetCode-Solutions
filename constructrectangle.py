class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # L >= W
        # Difference Between L and W should be as small as possible
        res = [float('-inf'), float('inf')]
        for w in range(int(area**0.5), 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]
