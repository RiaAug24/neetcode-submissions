class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = {}
        for x in nums:
            if x not in nums_dict.keys():
                nums_dict[x] = 1
                continue
            return x
        
                
        