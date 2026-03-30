class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def linearRob(cost):
            n = len(cost)
            dp = [0]*len(cost)
            dp[0] = cost[0]
            dp[1] = max(cost[0], cost[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1], dp[i-2]+cost[i])
            return dp[n-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(linearRob(nums[0:n-1]), linearRob(nums[1:n]))