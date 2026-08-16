class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        def get_neighbors(node):
            x,y = node
            results = []
            for dx,dy in [(0,1),(1,0), (-1,0),(0,-1)]:
                nr,nc = x+dx, y+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                    results.append((nr,nc))

            return results

        def bfs():
            nonlocal fresh 
            if not q:
                return 0
            total_time = -1
            while q:
                total_time += 1
                for i in range(len(q)):
                    node = q.popleft()
                    for neighbor in get_neighbors(node):
                        q.append(neighbor)
                        grid[neighbor[0]][neighbor[1]] = 2
                        fresh -= 1
            return total_time
    
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        totalTime = bfs()
        return totalTime if not fresh else -1
    