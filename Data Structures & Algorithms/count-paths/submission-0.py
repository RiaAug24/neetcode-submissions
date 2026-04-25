class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(i, j):
            if i == m or j == n:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            res = dfs(i+1, j) + dfs(i, j+1)

            return res
        
        return dfs(0, 0)