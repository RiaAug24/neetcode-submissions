"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeCopies = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            nodeCopies[cur] = copy
            cur = cur.next
        temp = head
        dummy = newNode = Node(0)
        while temp:
            copy = nodeCopies[temp]
            copy.next = nodeCopies[temp.next]
            copy.random = nodeCopies[temp.random]
            newNode.next = copy
            newNode = newNode.next
            temp = temp.next
        return dummy.next
