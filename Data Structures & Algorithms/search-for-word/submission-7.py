class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == "":
            return True

        m,n = len(board), len(board[0])
        b = len(word)
        def dfs(start, sofar, visited):
            if sofar == b:
                return True
            
            r,c = start
            for x,y in [(0,-1),(-1,0),(0,1),(1,0)]:
                nr,nc = x+r, y+c
                if 0<=nr<m and 0<=nc<n and (nr,nc) not in visited and board[nr][nc] == word[sofar]:
                    visited.append((nr,nc))
                    if dfs((nr,nc), sofar+1, visited):
                        return True
                    visited.pop()


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs((i,j),1, [(i,j)]):
                        return True
        
        return False
        
