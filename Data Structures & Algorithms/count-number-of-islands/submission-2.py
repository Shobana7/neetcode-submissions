class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m,n = len(grid), len(grid[0])
        num_of_islands = 0

        def get_neighbor_nodes(node):
            delta = [(0,1), (1,0), (0,-1),(-1,0)]
            x,y = node
            results = []
            for dx,dy in delta:
                nr,nc = x+dx, y+dy
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
                    results.append((nr,nc))
            return results


        def dfs(root):
            x,y = root
            grid[x][y] = '0'

            for neighbor in get_neighbor_nodes((x,y)):
                dfs(neighbor)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_of_islands += 1
                    dfs((i,j))
        
        return num_of_islands