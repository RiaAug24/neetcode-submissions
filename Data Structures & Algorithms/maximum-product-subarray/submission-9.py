class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_ = max_ = nums[0]
        res = nums[0]
        print("min:", min_)
        print("max:", max_)
        for num in nums[1:]:
            print("num:", num)
            temp_min = min_
            temp_max = max_
            if num != 0:
                min_ = min(temp_min * num, temp_max * num, num)
                max_ = max(temp_max * num, temp_min * num, num)
                res = max(res, max_)
            else:
                min_= 1
                max_ = 1
                res = max(res, 0)
            print("min:", min_)
            print("max:", max_)
            

        return res
            
        
                


            
           

      
        



                 
        