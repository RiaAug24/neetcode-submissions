# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or not (root.left or root.right):
            return 0
        res = 0
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                lng_path = self.findDepth(node.left) + self.findDepth(node.right)    
                res = max(res, lng_path)
        return res
        
    def findDepth(self, node):
        stack = [[node, 1]]
        d = 0
        while stack:
            node, depth = stack.pop(0)
            if node:
                if node.left:
                    stack.append([node.left, depth+1])
                if node.right:
                    stack.append([node.right, depth+1])
                d = max(d, depth)
        return d    

            

            



    
        