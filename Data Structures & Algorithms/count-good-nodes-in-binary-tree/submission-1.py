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
        self.ancestor_dict = {root: [root.val]}
        self.res = 1
        def dfs(root):
            if not root:
                return
            if root.left:
                self.ancestor_dict[root.left] = self.ancestor_dict[root] + [root.val]
                if root.left.val >= max(self.ancestor_dict[root.left]):
                    self.res += 1
                dfs(root.left)
            if root.right:
                self.ancestor_dict[root.right] = self.ancestor_dict[root] + [root.val]
                if root.right.val >= max(self.ancestor_dict[root.right]):
                    self.res += 1
                dfs(root.right)
        dfs(root)
        print(self.ancestor_dict)
        return self.res

