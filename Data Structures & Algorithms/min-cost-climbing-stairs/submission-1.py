class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost) + 1

        dp = [0]*(n+1)
        
        dp[0] = 0
        dp[1] = 0
        dp[2] = 0
        for i in range(3,n+1):
            dp[i] = min(dp[i-1] + cost[i-2] , dp[i-2] + cost[i-3])
        
        return dp[n]