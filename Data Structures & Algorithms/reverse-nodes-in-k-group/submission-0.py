# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth_node = self.findKthNode(groupPrev, k)
            if not kth_node:
                break
            groupNext = kth_node.next
            prev, cur = kth_node.next, groupPrev.next
            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = groupPrev.next
            groupPrev.next = kth_node
            groupPrev = temp
            
        return dummy.next


    def findKthNode(self, cur, k) -> Optional[ListNode]:
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur


    
        
            
            

            
                     


        