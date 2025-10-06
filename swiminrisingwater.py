class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[inf] * n for _ in range(n)]
        dist[0][0] = grid[0][0]

        heap = [(grid[0][0], 0, 0)]

        while heap:
            cost, r, c = heappop(heap)
            if (r, c) == (n-1, n-1):
                return cost

            if cost > dist[r][c]:
                continue

            for(dirrow, dircol) in [(1,0), (-1,0), (0,1), (0,-1)]:
                neighborrow, neighborcol = r + dirrow, c + dircol
                if 0 <= neighborrow < n and 0 <= neighborcol < n:
                    neighborheight = grid[neighborrow][neighborcol]

                    newMaxHeight = max(cost, neighborheight)

                    if newMaxHeight < dist[neighborrow][neighborcol]:
                        dist[neighborrow][neighborcol] = newMaxHeight
                        heappush(heap, (newMaxHeight, neighborrow, neighborcol))
