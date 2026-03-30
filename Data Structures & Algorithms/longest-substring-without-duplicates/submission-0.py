class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0,0
        seen = {}
        maxLen = 0
        while r < len(s):
            if s[r] not in seen or seen[s[r]] == 0:
                seen[s[r]] = 1
                maxLen = max(maxLen, (r-l)+1)
                r += 1
            else:
                while l < r and seen[s[r]] > 0:
                    seen[s[l]] -= 1
                    l += 1
        
        return maxLen

