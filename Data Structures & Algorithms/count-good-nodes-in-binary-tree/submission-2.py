# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.root_dict = {root: root.val}
        self.res = 1
        def dfs(root):
            if not root:
                return
            if root.left:
                if root.left.val >= self.root_dict[root] and root.left.val >= root.val:
                    self.res += 1
                    self.root_dict[root.left] = root.left.val
                else:
                    self.root_dict[root.left] = self.root_dict[root]
                dfs(root.left)
            if root.right:
                if root.right.val >= self.root_dict[root] and root.right.val >= root.val:
                    self.res += 1
                    self.root_dict[root.right] = root.right.val
                else:
                    self.root_dict[root.right] = self.root_dict[root]
               
                dfs(root.right)
        dfs(root)
        return self.res

