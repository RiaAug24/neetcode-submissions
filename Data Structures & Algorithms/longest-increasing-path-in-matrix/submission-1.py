class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(i, j, prev, visit):
            if i < 0 or i == rows or j < 0 or j == cols or (i, j) in visit or (matrix[i][j] <= prev and prev != -1):
                return 0
            
            visit.add((i, j))
            res = max(1+ dfs(i+1, j, matrix[i][j], visit), 1 + dfs(i-1, j, matrix[i][j], visit), 1 + dfs(i, j+1, matrix[i][j], visit), 1 + dfs(i, j-1, matrix[i][j], visit))
            visit.remove((i, j))
            return res
        
        
        
        maxLen = 0

        for r in range(rows):
            for c in range(cols):
                maxLen = max(maxLen, dfs(r, c, -1, set([])))
                print("maxlen", maxLen)
        return maxLen
                
        