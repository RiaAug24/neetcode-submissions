class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        cur_sum = nums[0]
        max_sum = -math.inf
        
        for i in range(1, len(nums)):
            max_sum = max(max_sum, cur_sum)
            if cur_sum + nums[i] <= nums[i]:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
        
        return max(max_sum, cur_sum)



   

        