class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        freq = [0]*26
        maxFreq = 0
        maxLen = 0
        while r < len(s):  
            key = ord(s[r])-ord('A')
            freq[key] += 1
            maxFreq = max(maxFreq,freq[key])
            while l < r and (r-l + 1 - maxFreq) > k:
                freq[ord(s[l])-ord('A')] -= 1
                maxFreq = max(freq)
                l += 1
            maxLen = max(maxLen, (r-l)+1)
            r += 1
        
        return maxLen
            

