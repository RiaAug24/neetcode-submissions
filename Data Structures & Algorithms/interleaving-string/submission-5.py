class Solution:
    from functools import lru_cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)] = True
        print(dp)
    
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True

                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]



        # def backtrack(i, j, itl_str):

        #     nonlocal res1, res2, res3

        #     if (i, j, itl_str) in cache:
        #         return cache[(i, j, itl_str)]

        #     if i == len(s1) and j == len(s2):
        #         if itl_str == s3:
        #             print(itl_str)
        #             return True
        #         return False
            
        #     if i < len(s1):
        #         res1 = backtrack(i+1, j, itl_str + s1[i])

        #     if j < len(s2):
        #         res2 = backtrack(i, j+1, itl_str + s2[j])

        #     if i < len(s1) and j < len(s2):
        #         res3 = backtrack(i+1, j+1, itl_str + s1[j] + s2[j])
            
        #     cache[(i, j, itl_str)] = res1 or res2 or res3

        #     return cache[(i, j, itl_str)] 
           
        # return backtrack(0, 0, "")


            

        