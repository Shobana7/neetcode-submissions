class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islandCount = 0
        m,n = len(grid), len(grid[0])

        def dfs(x,y):
            grid[x][y] = '0'

            for i,j in [(-1,0),(0,-1),(1,0),(0,1)]:
                dx, dy = x + i, y + j
                if 0<=dx<m and 0<=dy<n and grid[dx][dy] == '1':
                    dfs(dx,dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandCount += 1
                    dfs(i,j)
        
        return islandCount