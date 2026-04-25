class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]

            if i == len(nums) - 1:
                return True
            
            if i > len(nums)-1:
                return False
                
            k = 1

            while k <= nums[i]:
                cache[i] = dfs(i+k)
                if cache[i]:
                    return cache[i]
                else:
                    k +=1
            return False

        
        return dfs(0)
        