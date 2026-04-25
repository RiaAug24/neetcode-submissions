class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums_dict = {}
        # for x in nums:
        #     if x not in nums_dict.keys():
        #         nums_dict[x] = 1
        #         continue
        #     return x
        for i in range(0, len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
            
            
                
        