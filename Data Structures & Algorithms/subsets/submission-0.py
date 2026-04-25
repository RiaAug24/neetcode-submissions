class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        firstEle = nums[0]
        remainingEle = nums[1:]

        generated_subsets = self.subsets(remainingEle)
        res = []
        for subset in generated_subsets:
            res.append(subset)
            res.append([firstEle] + subset)
        return res

        