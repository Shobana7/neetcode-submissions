class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        min_len = float('inf')
        pos = (-1,-1)
        matches = 0
        freq_t = Counter(t)
        s_freq = defaultdict(int)

        for i in range(len(t)):
            s_freq[s[i]] += 1
            if s[i] in freq_t and s_freq[s[i]] == freq_t[s[i]]:
                matches += 1

        if matches == len(freq_t):
            return s[:len(t)]
        
        l,r = 0,i+1
        
        while r < len(s):
            s_freq[s[r]] += 1
            if s[r] in freq_t and s_freq[s[r]] == freq_t[s[r]]:
                matches += 1
                while l <= r and matches == len(freq_t):
                    if min_len > (r-l + 1):
                        min_len = (r-l+1)
                        pos = (l,r)
                    s_freq[s[l]] -= 1
                    if s[l] in freq_t and s_freq[s[l]] < freq_t[s[l]]:
                        matches -= 1
                        print(matches)
                    l += 1
            r += 1
        

        return s[pos[0]:pos[1]+1]


                    
                    


        
