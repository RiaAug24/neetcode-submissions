# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val == root.val or q.val == root.val:
            return root

        self.parents = {
            p: [root],
            q: [root]
        }
        
        def dfs(root, node):
            if not root:
                return None
            if root.val == node.val:
                if root not in self.parents[node]:
                    self.parents[node].append(root)
                return
            if node.val < root.val:
                if root.left not in self.parents[node]:
                    self.parents[node].append(root.left)
                return dfs(root.left, node)
            else:
                if root.right not in self.parents[node]:
                    self.parents[node].append(root.right)
                return dfs(root.right, node)
        dfs(root, p)
        dfs(root, q)
        print(self.parents)
        lcp = [x for x in self.parents[p] if x in self.parents[q]]
        print(lcp)
        return lcp[-1]




            


            
        
        