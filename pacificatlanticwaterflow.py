class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        n = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(i, j, visited):
            visited.add((i, j))

            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < len(heights) and 0 <= y < n:
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x, y, visited)
                
        p, a = set(), set()

        for j in range(n):
            dfs(0, j, p)
        for i in range(len(heights)):
            dfs(i, 0, p)
        for j in range(n):
            dfs(len(heights)-1, j, a)
        for i in range(len(heights)):
            dfs(i, n-1, a)

        return list(p & a)
