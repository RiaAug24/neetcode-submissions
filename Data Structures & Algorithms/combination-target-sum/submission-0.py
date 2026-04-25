class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(cur_sum, arr, i):
            if cur_sum > target or i == len(nums):
                return

            if cur_sum == target:
                print(arr, cur_sum, i)
                a = arr.copy()
                res.append(a)
                return
        
            arr.append(nums[i])
            cur_sum += nums[i]
            dfs(cur_sum, arr, i)

            arr.pop()
            cur_sum -= nums[i]
            dfs(cur_sum, arr, i+1)

        dfs(0, [], 0)

        return res
