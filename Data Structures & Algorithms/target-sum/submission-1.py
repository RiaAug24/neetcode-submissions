class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, sum_):

            if i == len(nums):
                return 1 if sum_ == target else 0

            res = dfs(i+1, sum_+nums[i]) + dfs(i+1, sum_-nums[i])
            return res
        
        return dfs(0, 0)


        