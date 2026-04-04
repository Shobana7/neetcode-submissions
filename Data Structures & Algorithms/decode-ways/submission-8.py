class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0]*len(s)
        if s[0] != '0':
            dp[0] = 1
        else:
            return 0
        
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] in '12':
                    dp[i] = dp[i-2] if i-2 >= 0 else 1
                else:
                    return 0
            else:
                if (s[i-1] == '1') or s[i-1] == '2' and s[i] in '0123456':
                    dp[i] = dp[i-1] + dp[i-2] if i-2 >= 0 else  dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]

        
        return dp[len(s)-1]
            
