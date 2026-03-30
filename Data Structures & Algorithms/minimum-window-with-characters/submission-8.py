class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_map = Counter(t)
        minLen = float('inf')
        l,r = 0,0
        res_l , res_r = float('inf'), float('inf')
        s_map = defaultdict(int)
        match = 0
        while r < len(s):
            if s[r] in t_map:
                s_map[s[r]] += 1
                if s_map[s[r]] == t_map[s[r]]:
                    match += 1
                    while l <= r and match == len(t_map):
                        if (r-l+1) < minLen:
                            minLen = r-l+1
                            res_l , res_r = l ,r
                    
                        s_map[s[l]] -= 1
                        if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                            match -= 1
                        l += 1
                        
            r += 1
        
        return s[res_l:res_r+1] if res_l != float('inf') else ""
