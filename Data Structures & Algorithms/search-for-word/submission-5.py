class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        self.found = False
        def backtrack(row, col, s, seen,w):
            print(s)
            if s == word:
                self.found = True
                return 
            
            for x,y in [(-1,0),(0,-1),(1,0),(0,1)]:
                nr = row + x
                nc = col + y
                if  0<=nr < m and 0<=nc < n:
                    if (nr,nc) not in seen:
                        if board[nr][nc] == word[w]:
                            seen.add((nr,nc))
                            backtrack(nr,nc, s + word[w],seen, w + 1)
                            seen.remove((nr,nc))


        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    seen = set()
                    seen.add((i,j))
                    backtrack(i,j, word[0], seen,1)
                    if self.found: 
                        return True
        
        return self.found