class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [(0,-1),(-1,0),(0,1),(1,0)]
        m,n = len(grid), len(grid[0])
        max_area = 0

        def calc_area(start):
            q = deque()
            q.append(start)
            grid[start[0]][start[1]]=0
            area = 1
            while q:
                r,c = q.popleft()
                for x, y in directions:
                    nr,nc = r+x,c+y
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        grid[nr][nc]=0
                        area+=1
                        q.append((nr,nc))
                
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = calc_area((i,j))
                    max_area = max(max_area, area)
        
        return max_area
