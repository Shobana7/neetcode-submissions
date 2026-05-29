class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(sumSoFar,j, path):
            if sumSoFar == target:
                res.append(path[:])
                return
            
            for i in range(j, len(nums)):
                if sumSoFar + nums[i] > target:
                    continue
                path.append(nums[i])
                dfs(sumSoFar + nums[i],i, path)
                path.pop()
        
        dfs(0,0,[])

        return res