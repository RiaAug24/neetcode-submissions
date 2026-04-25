class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        
        
        def dfs(i, j, area):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return area
            area += 1
            grid[i][j] = 0
            area = dfs(i+1, j, area)
            area = dfs(i-1, j, area)
            area = dfs(i, j+1, area)
            area = dfs(i, j-1, area)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j, 0))
        return maxArea
        