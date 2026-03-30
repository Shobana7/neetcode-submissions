class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        q = deque()

        def bfs():
            level = 0
            while q:
                t = len(q)
                level += 1
                for i in range(t):
                    r, c = q.popleft()
                    for x, y in [(0,-1),(-1,0),(0,1),(1,0)]:
                        nr, nc = r+x, c+y
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc] > 0 and grid[nr][nc] > level:
                            grid[nr][nc] = level
                            q.append((nr,nc))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))

        bfs()