class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        def backtrack(i, j):
            
            if j >= len(t):
                return 1

            if i == len(s):
                return 0

            res = backtrack(i+1, j)
            if s[i] == t[j]:
                res += backtrack(i+1, j+1)

            return res
        
        return backtrack(0, 0)



        