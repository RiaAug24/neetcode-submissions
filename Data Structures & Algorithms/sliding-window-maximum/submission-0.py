class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_ele = []
        n = len(nums)
        i = 0
        j = k
        while j <= n:
            max_ele.append(max(nums[i:j]))
            i += 1
            j += 1
        return max_ele
        