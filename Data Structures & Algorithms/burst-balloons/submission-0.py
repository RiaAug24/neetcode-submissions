class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        res = 0
        def dfs(cur, arr):
            nonlocal res

            if len(arr) == 1:
                res = max(res, cur + arr[0])
                return

            elif len(arr) > 2:
                for i in range(len(arr)):
                    temp = arr.copy()
                    if i > 0 and i < len(arr)-1:
                        temp.pop(i)
                        dfs(cur + arr[i-1] * arr[i] * arr[i+1], temp)
                    elif i == 0:
                        temp.pop(0)
                        dfs(cur + arr[i] * arr[i+1], temp)
                    else:
                        temp.pop(-1)
                        dfs(cur + arr[i-1] * arr[i], temp)
            else:
                temp1 = arr.copy()
                temp2 = arr.copy()
                temp1.pop(0)
                dfs(cur + arr[0] * arr[1], temp1)
                temp2.pop(-1)
                dfs(cur + arr[0] * arr[1], temp2)

        dfs(0, nums)

        return res
            
            
