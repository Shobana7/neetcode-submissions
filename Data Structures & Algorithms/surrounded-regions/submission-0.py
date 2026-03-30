class Solution:                                           
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def bfs(start):
            q = deque()
            q.append(start)

            while q:
                r,c = q.popleft()
                for x, y in [(0,-1),(-1,0),(0,1),(1,0)]:
                    nr,nc = x+r, y+c
                    if 0<=nr<m and 0<=nc<n and board[nr][nc] == 'O':
                        board[nr][nc] = 'A'
                        q.append((nr,nc))
                

        for i in range(m):
            for j in range(n):
                if i in [0, m-1] or j in [0,n-1]:
                    if board[i][j] == 'O':
                        board[i][j] = 'A'
                        bfs((i,j))    


        for i in range(m):
            for j in range(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    if board[i][j] == 'A':
                        board[i][j] = 'O'                            