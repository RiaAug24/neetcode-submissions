class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= n and j >= m:
                cache[(i, j)] = True
                return cache[(i, j)]
            
            if j >= m:
                cache[(i, j)] = False
                return cache[(i, j)]
            
            matchFound = i < n and (s[i] == p[j] or p[j] == ".")
            if j + 1 < m and p[j+1] == "*":
                cache[(i, j)] = (dfs(i, j+2) or (matchFound and dfs(i+1, j)))
                return cache[(i, j)]
            
            if matchFound:
                cache[(i, j)] = dfs(i+1, j+1)
                return cache[(i, j)]
            
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

        
