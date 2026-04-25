class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])


        return dp[0][0]

        # def backtrack(i, j, count):
        
        #     if i >= len(text1) or j >= len(text2):
        #         return count

            
        #     if text1[i] ==  text2[j]:
        #         return backtrack(i+1, j+1, count + 1) 
                
        #     dp[i][j] = max(backtrack(i+1, j, count), backtrack(i, j+1, count))
        #     return dp[i][j]

        # return backtrack(0, 0, 0)



                    



        