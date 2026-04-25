class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, sum_):

            if sum_ == target and i == len(nums):
                return 1
            
            if i == len(nums):
                return 0

            res = dfs(i+1, sum_+nums[i]) + dfs(i+1, sum_-nums[i])
            return res
        
        return dfs(0, 0)


        