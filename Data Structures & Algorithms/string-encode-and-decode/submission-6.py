class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for w in strs:
            lengthOfStr = len(w)
            encoded_string += str(lengthOfStr) + "#" + w
        
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        answer = []

        i = 0 
        while i < len(s):
            j = i
            lengthOfStr = ""
            while s[j] != "#":
                lengthOfStr += s[j]
                j +=1
            j += 1
            word = ""
            k = 0
            while k < int(lengthOfStr):
                word += s[j]
                k += 1
                j += 1
            answer.append(word)
            i = j
        
        return answer
