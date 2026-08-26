class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        fresh = 0

        def get_neighbors(node):
            x,y = node
            result = []
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = x +dx, y+dy
                if 0<=nx<m and 0<=ny<n and grid[nx][ny] == 1:
                    result.append((nx,ny))
            return result

        def bfs():
            nonlocal fresh
            if not q:
                return 0
            total_time = -1
            while q:
                total_time += 1
                for i in range(len(q)):
                    node = q.popleft()
                    for neigh in get_neighbors(node):
                        a,b = neigh
                        grid[a][b] = 2
                        fresh -= 1
                        q.append((a,b))
            return total_time


        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        totalTime = bfs()
        return totalTime if fresh == 0 else -1