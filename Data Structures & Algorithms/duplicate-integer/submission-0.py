class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lookup = {}

        for i in range(len(nums)):
            if nums[i] in lookup:
                return True
            lookup[nums[i]] = i
        
        return False