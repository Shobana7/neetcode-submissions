class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mp = defaultdict(int)
        max_length = 0

        for i in nums:
            if not mp[i]:
                mp[i] = mp[i-1]+mp[i+1]+1
                mp[i-mp[i-1]] = mp[i]
                mp[i+mp[i+1]] = mp[i]
                max_length = max(max_length, mp[i])
        
        return max_length


