class Solution:
    def rob(self, nums: List[int]) -> int:
        res = max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

        return res

    def helper(self, nums):
        rob1 = rob2 = 0

        for n in nums:
            nextRob = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = nextRob
        
        return rob2
                
                
            


        