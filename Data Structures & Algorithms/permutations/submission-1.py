class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
         
        res = []
        length = len(nums)
        seen = set()

        def backtrack(i, path):
            if length == len(path):
                res.append(path.copy())
                return
            
            for j in range(length):
                if nums[j] in seen:
                    continue
                path.append(nums[j])
                seen.add(nums[j])
                backtrack(j+1, path)
                path.pop()
                seen.remove(nums[j])
        
        backtrack(0,[])
        return res

