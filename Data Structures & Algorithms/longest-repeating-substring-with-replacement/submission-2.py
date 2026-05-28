class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l,r = 0,0
        freq = defaultdict(int)
        maxLen = 0
        maxFreq = 0

        while r < len(s):
            freq[s[r]] += 1
            maxFreq = max(maxFreq, freq[s[r]])

            while l<r and (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                maxFreq = max(maxFreq, freq[s[l]])
                l += 1
            maxLen = max(maxLen, r-l+1)

            r += 1

        return maxLen