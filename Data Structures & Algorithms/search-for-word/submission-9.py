class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True

        m,n = len(board), len(board[0])
        b = len(word)
        def dfs(start, sofar):
            if sofar == b:
                return True
            
            r,c = start
            board[r][c] = '#'
            for x,y in [(0,-1),(-1,0),(0,1),(1,0)]:
                nr,nc = x+r, y+c
                if 0<=nr<m and 0<=nc<n and board[nr][nc] != '#' and board[nr][nc] == word[sofar]:
                    if dfs((nr,nc), sofar+1):
                        return True
            board[r][c] = word[sofar-1]


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs((i,j),1):
                        return True
        
        return False
        
