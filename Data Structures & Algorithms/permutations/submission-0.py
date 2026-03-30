class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        res = []
        length = len(nums)

        def backtrack(i, path):
            if length == len(path):
                res.append(path.copy())
                return
            
            for j in range(length):
                if nums[j] in path:
                    continue
                path.append(nums[j])
                backtrack(j+1, path)
                path.pop()
        
        backtrack(0,[])
        return res

