class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        reach = [[""]*len(heights[0]) for j in range(len(heights))]
        m = len(heights)
        n = len(heights[0])

        for i in range(len(heights[0])):
            reach[0][i] += "P"
            reach[len(heights)-1][i] += "A"

        for i in range(len(heights)):
            reach[i][0] += "P"
            reach[i][len(heights[0])-1] += "A"


        def dfs(start, ocean):
            r,c = start
            ht = heights[r][c]
            for (x,y) in [(0,-1),(-1,0),(0,1),(1,0)]:
                nr,nc = r+x, c+y
                if 0<=nr<m and 0<=nc<n and ht <= heights[nr][nc] and ocean not in reach[nr][nc]:
                    reach[nr][nc] += ocean
                    dfs((nr,nc), ocean)


        for i in range(n):
            dfs((0,i), "P")
            dfs((m-1, i), "A")        

        for i in range(m):
            dfs((i,0), "P")
            dfs((i,n-1), "A")    

        print(reach)
        res = []
        for i in range(m):
            for j in range(n):
                if "P" in reach[i][j] and "A" in reach[i][j]:
                    res.append((i,j))
        return res
