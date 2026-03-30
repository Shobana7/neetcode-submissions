class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        maxMin = 0
        q = deque()
        fresh = 0

        def bfs():
            nonlocal fresh
            if not q:
                return 0
            minutes = -1

            while q:
                minutes += 1
                t = len(q)
                for i in range(t):
                    r,c = q.popleft()
                    for x, y in [(-1,0),(0,1),(1,0),(0,-1)]:
                        nr,nc = r+x, c+y
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                            q.append((nr,nc))
                            fresh -= 1
                            grid[nr][nc] = 0
            return minutes

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    grid[i][j] = 0
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        maxMin = bfs()

        
        return maxMin if not fresh else -1