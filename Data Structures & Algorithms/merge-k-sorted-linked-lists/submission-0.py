# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return
        dummy = newHead = ListNode()
        dummy.next = newHead
        merged_list = []
        for k in lists:
            temp = k
            while temp:
                merged_list.append(temp.val)
                temp = temp.next
        for x in sorted(merged_list):
            newHead.next = ListNode(x)
            newHead = newHead.next
        return dummy.next

        