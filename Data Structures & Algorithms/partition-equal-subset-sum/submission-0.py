class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        N = len(nums)
        if sum(nums) % 2 != 0: return False

        half_ = sum(nums) // 2
        
        res = False

        def dfs(i, cur):
            nonlocal res

            if cur == half_ :
                res = True
                return
            
            if cur > half_ or i == N:
                return

            cur += nums[i]
            dfs(i+1, cur)
            
            cur -= nums[i]
            dfs(i+1, cur)
        
        dfs(0, 0)
        return res


            

          

          

        return res





        