class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        if not s2 or len(s2) < len(s1):
            return False

        s1mp = Counter(s1)
        s2mp = defaultdict(int)
        match = 0
        l,r=0,0
        for r in range(len(s1)):
            s2mp[s2[r]] += 1
            if s2mp[s2[r]] == s1mp[s2[r]]:
                match += 1
        
        if match == len(s1):
            return True
        if s2mp[s2[l]] == s1mp[s2[l]]:
            match -= 1
        s2mp[s2[l]] -= 1
        l += 1
        r += 1

        
        while r < len(s2):
            s2mp[s2[r]] += 1 
            print(s2[r],s2mp[s2[r]], match)
            if s2mp[s2[r]] == s1mp[s2[r]]:
                match += 1
                print(s2mp, match)
                if match == len(s1mp):
                    return True
            
            if s2mp[s2[l]] == s1mp[s2[l]]:
                match -= 1
            s2mp[s2[l]] -= 1
            l += 1

            r += 1
        
        return False
            



            




