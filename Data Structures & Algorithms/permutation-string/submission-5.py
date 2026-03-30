class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1mp = [0]*26
        s2map = [0]*26

        for r in range(len(s1)):
            s1mp[ord(s1[r]) -ord('a')] += 1
            s2map[ord(s2[r]) -ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches +=( 1 if s1mp[i] == s2map[i] else 0)

        l = 0
        r += 1
        while r < len(s2):
            if matches == 26:
                return True
            idx = ord(s2[r]) - ord('a')
            s2map[idx] += 1

            if s2map[idx] == s1mp[idx]:
                matches += 1
            elif s2map[idx] == s1mp[idx] + 1:
                matches -=1 

            idx = ord(s2[l]) - ord('a')
            s2map[idx] -= 1

            if s2map[idx] == s1mp[idx]:
                matches += 1
            elif s2map[idx] == s1mp[idx] - 1:
                matches -=1 

            l += 1
            r += 1
        
        return matches == 26