class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        

    def add(self, val: int) -> int:
        self.nums.append(val)           
        self.nums = sorted(self.nums, reverse=True)
            
            
        if self.k > len(self.nums):
            return self.nums[-1]
        
        return self.nums[self.k-1]


        
        
