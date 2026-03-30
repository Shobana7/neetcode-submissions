class Solution:

    def encode(self, strs: List[str]) -> str:

        s = ""

        for i in strs:
            l = len(i)
            s += str(l)+"#"+i
        
        return s

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            l = ""
            while s[i] != '#':
                l += s[i]
                i += 1
            print(l)
            length = int(l)
            i +=1 
            res.append(s[i:i+length])
            i += length
            print(res, i)
        
        return res



            


