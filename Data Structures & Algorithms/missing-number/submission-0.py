class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        totalSum = n *(n-1) // 2
        sum_so_far = 0

        for i in nums:
            sum_so_far += i
        
        return totalSum - sum_so_far