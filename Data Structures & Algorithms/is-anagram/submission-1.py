class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sig1 = [0]*26
        sig2 = [0]*26

        for i in range(len(s)):
            sig1[ord(s[i])-ord('a')] +=1 
            sig2[ord(t[i])-ord('a')] +=1 
        
        return sig1 == sig2