class Solution:
    def rob(self, cost: List[int]) -> int:
        
        n = len(cost)
        if n == 1:
            return cost[0]

        dp = [0]*n
        dp[0] = cost[0]
        dp[1] = max(dp[0], cost[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2]+cost[i])
        
        return dp[n-1]
