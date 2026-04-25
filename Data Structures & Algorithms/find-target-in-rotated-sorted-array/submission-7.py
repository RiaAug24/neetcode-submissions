class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            mid = int((l + r) / 2)
            if nums[mid] == target:
                return mid
            elif nums[r] > nums[mid] and target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1