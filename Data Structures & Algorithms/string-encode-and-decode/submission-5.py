class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            x = len(s)
            res.append(str(x)+"#"+s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1

            word = ""
            j = 0
            while j < int(length):
                word += s[i]
                i += 1
                j += 1

            res.append(word)
        
        return res




