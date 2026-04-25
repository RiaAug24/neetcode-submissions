class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 1:
        #     return 1
        
        # res = self.climbStairs(n-1) + self.climbStairs(n-2)
        # return res
    
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


        