# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            self.res = max(self.res, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.res

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     if not root or not (root.left or root.right):
    #         return 0
    #     res = 0
    #     stack = [root]
    #     while stack:
    #         node = stack.pop(0)
    #         if node:
    #             if node.left:
    #                 stack.append(node.left)
    #             if node.right:
    #                 stack.append(node.right)
    #             path = self.dfs(node.left) + self.dfs(node.right)    
    #             res = max(res, path)
    #     return res
        
    # def dfs(self, node):
    #     stack = [[node, 1]]
    #     d = 0
    #     while stack:
    #         node, depth = stack.pop(0)
    #         if node:
    #             if node.left:
    #                 stack.append([node.left, depth+1])
    #             if node.right:
    #                 stack.append([node.right, depth+1])
    #             d = max(d, depth)
    #     return d    

            

            



    
        