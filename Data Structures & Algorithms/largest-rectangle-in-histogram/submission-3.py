class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)
        for i, x in enumerate(heights):
            if len(stack) == 0:
                stack.append([i, x])
                max_area = x
                continue
            idx = i
            while stack and stack[-1][1] > x:
                idx, height = stack.pop()
                max_area = max(max_area, (i - idx) * height)
            stack.append([idx, x])
        for x in stack:
            max_area = max(max_area, (n - x[0]) * x[1])
        return max_area



        