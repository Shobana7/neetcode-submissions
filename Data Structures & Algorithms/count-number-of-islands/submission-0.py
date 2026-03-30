class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        count = 0
        m,n = len(grid), len(grid[0])

        def get_neighbors(node):
            r,c = node
            res =[]
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr,nc = r+x, c+y
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
                    res.append((nr,nc))
            
            return res


        def count_islands(start):
            q = deque()
            q.append(start)
        
            while q:
                x,y = q.popleft()
                grid[x][y] = "-1"
                for r,c in get_neighbors((x,y)):
                    q.append((r,c))




        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    count_islands((i,j))

        return count
