# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = 0
        temp = root
        visited = []
        stack = [[temp, 1]]
        depth = 0
        while stack:
            node, depth = stack.pop(0)
            if node not in visited:
                visited.append(node)
                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth + 1])
                max_depth = max(max_depth, depth)
        return max_depth
            


        