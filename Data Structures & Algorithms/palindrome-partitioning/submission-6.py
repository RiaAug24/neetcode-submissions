class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.checkPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        dfs(0)
        return res
    
    def checkPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     res = []
    #     n = len(s)
    #     if n == 1:
    #         res.append([s])
    #         return res
    #     for k in range(0, n):
    #         arr = []
    #         i = 0
    #         j = k + 1
    #         prev_range = []
    #         if len(s[i:j]) == n:
    #             if self.checkPalindrome(s[i:j]):
    #                 res.append([s[i:j]])
    #         else:
    #             while i < n:
    #                 print(i, j)
    #                 print(s[i:j])
    #                 if i not in prev_range:
    #                     if self.checkPalindrome(s[i:j]):
    #                         arr.append(s[i:j])
    #                         prev_range = [x for x in range(i,j)]
    #                     else: 
    #                         arr.append(s[i])
    #                 i += 1
    #                 j += 1
    #             if arr not in res:
    #                 res.append(arr) 
    #     return res

    
    
        