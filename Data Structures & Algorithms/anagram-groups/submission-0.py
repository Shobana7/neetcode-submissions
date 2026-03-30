class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        group = defaultdict(list)

        for s in strs:
            group[tuple(sorted(s))].append(s)
        
        return list(group.values())
