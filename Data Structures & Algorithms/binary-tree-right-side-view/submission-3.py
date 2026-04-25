# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [[root, 0]]
        level = []
        while queue:
            node, depth = queue.pop(0)
            if node:
                queue.append([node.left, depth+1])
                queue.append([node.right, depth + 1])
            
                if depth < len(level):
                    level[depth].append(node.val)
                else:
                    level.append([node.val])

        res = []
        for x in level:
            res.append(x[-1])
        return res


                

        