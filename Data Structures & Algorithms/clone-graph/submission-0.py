"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        oldToNew = {}

        def clone(cur):
            if cur in oldToNew:
                return oldToNew[cur]
            
            copy = Node(cur.val)
            oldToNew[cur] = copy
            for n in cur.neighbors:
                copy.neighbors.append(clone(n))
            
            return copy
        
        return clone(node)
            


        