class Solution:
    def jump(self, nums: List[int]) -> int:

        def dfs(i, count):
            if i == len(nums)-1:
                return count

            if i >= len(nums):
                return math.inf
                
            res = math.inf
            for j in range(nums[i], 0, -1):
                print(i, j, i+j)
                res = min(res, dfs(i+j, count+1))
            
            return res
        return dfs(0, 0)

        