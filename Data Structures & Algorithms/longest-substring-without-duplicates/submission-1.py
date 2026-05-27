class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l,r = 0,0
        found = defaultdict(int)

        while r < len(s):
            if found[s[r]] == 0:
                found[s[r]] = 1
                maxLen = max(maxLen, r-l+1)
                r += 1
            else:
                while l < r and found[s[r]] != 0:
                    found[s[l]] -= 1
                    l += 1
        
        return maxLen
                