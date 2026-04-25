class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = int((l + r) / 2)
            print(nums[mid])
            if nums[mid] < min_val:
                min_val = nums[mid]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min_val

        