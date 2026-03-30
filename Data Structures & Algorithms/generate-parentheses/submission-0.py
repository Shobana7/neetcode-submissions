class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(openCount, closeCount, s):
            if len(s) == 2*n:
                res.append(s)
                return
            
            if openCount < n:
                backtrack(openCount + 1, closeCount, s + '(')
            
            if closeCount < openCount:
                backtrack(openCount , closeCount+1, s + ')')
        
        backtrack(0,0,'')
        return res

