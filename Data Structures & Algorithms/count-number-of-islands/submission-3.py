class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_count = 0
        m,n = len(grid),len(grid[0])

        def get_neighbors(node):
            x,y = node
            result = []
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx,ny = x+dx, y+dy
                if 0<= nx < m and 0<= ny < n and grid[nx][ny] == "1":
                    result.append((nx,ny))
            return result

        def bfs(start):
            q = deque()
            q.append(start)
            while q:
                for i in range(len(q)):
                    x,y = q.popleft()
                    for neighbor in get_neighbors((x,y)):
                        a,b = neighbor
                        grid[a][b] = "0"
                        q.append(neighbor)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    bfs((i,j))
                    island_count += 1
        
        return island_count