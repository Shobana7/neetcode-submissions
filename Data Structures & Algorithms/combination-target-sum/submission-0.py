class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        def backtrack(i, sum_so_far, path):
            if sum_so_far == target:
                res.append(path[:]) 
                return
            
            for j in range(i,len(nums)): 
                if sum_so_far + nums[j] > target:
                    continue
                
                path.append(nums[j])
                backtrack(j, sum_so_far + nums[j], path)
                path.pop()

        
        backtrack(0,0,[])
        return res
            

