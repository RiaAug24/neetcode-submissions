class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, arr, cur_s):

            if cur_s == target:
                res.append(arr.copy())
                return
            
            if i == len(candidates) or cur_s > target:
                return
            
            arr.append(candidates[i])
            dfs(i+1, arr, cur_s + candidates[i])
            arr.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, arr, cur_s)

        dfs(0, [], 0)
        return res
        