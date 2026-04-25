class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i, arr):

            if i == len(nums):
                a_cpy = sorted(arr.copy())
                if a_cpy not in res:
                    res.append(a_cpy)
                return
            
            arr.append(nums[i])
            dfs(i+1, arr)

            arr.pop()
            dfs(i+1, arr)
        
        dfs(0, [])
        return res

        