class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        n = len(nums)
        def backtrack(i, path):
            if i == n:
                res.add(tuple(path))
                return 
            
            for j in range(i, n):
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
                backtrack(j+1, path)
        
        nums.sort()
        backtrack(0,[])

        return list(res)