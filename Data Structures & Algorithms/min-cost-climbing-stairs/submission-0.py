class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        dp = cost + [0]
        for i in range(N-1, -1, -1):
            if i < N - 1:
                dp[i] = min(cost[i] + dp[i+1], cost[i] + dp[i+2])
            else:
                dp[i] = cost[i]
        return min(dp[0], dp[1])

