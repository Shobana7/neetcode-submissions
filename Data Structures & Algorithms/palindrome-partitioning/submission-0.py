class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                string = s[i:j+1]
                if string == string[::-1]:
                    path.append(string)
                    backtrack(j+1, path)
                    path.pop()
        
        backtrack(0,[])
        return res