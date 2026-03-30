class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = defaultdict(list)

        def backtrack(i, sum_so_far, path):
            if sum_so_far == target:
                res[tuple(path[:])].append(path[:])
                return
            
            for j in range(i, len(nums)):
                if sum_so_far + nums[j] > target:
                    continue
                
                path.append(nums[j])
                backtrack(j+1, sum_so_far+nums[j], path)
                path.pop()
        
        backtrack(0,0,[])

        result = []
        for k, v in res.items():
            result.append(list(k))
        return result