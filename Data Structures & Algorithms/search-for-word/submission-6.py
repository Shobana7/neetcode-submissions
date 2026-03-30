class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        self.found = False
        def backtrack(row, col, s,w):
            if s == word:
                self.found = True
                return 
            
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr = row + x
                nc = col + y
                if  0<=nr < m and 0<=nc < n:
                    if board[nr][nc] != "#":
                        if board[nr][nc] == word[w]:
                            board[nr][nc]= '#'
                            backtrack(nr,nc, s + word[w],w + 1)
                            board[nr][nc]= word[w]


        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    board[i][j] = '#'
                    backtrack(i,j, word[0], 1)
                    if self.found: 
                        return True
                    board[i][j] = word[0]
        
        return self.found