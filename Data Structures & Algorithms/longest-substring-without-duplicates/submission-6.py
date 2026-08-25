class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        chars_seen = set()
        l,r = 0,0

        while r < len(s):                
            while l < r and s[r] in chars_seen:
                chars_seen.remove(s[l])
                l += 1
            chars_seen.add(s[r])
            max_length = max(max_length, (r-l+1))
            r += 1
        
        return max_length
