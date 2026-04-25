class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
    
        prev = 0
        cur = nums[0]
        for i in range(1, n):
            temp = cur
            cur = max(prev + nums[i], cur)
            prev = temp
        return cur
            
        