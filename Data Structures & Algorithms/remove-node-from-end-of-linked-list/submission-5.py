# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not (head) or head.next == None:
            return None
        # temp = head
        # ListNodeLen = 0
        # while temp:
        #     ListNodeLen += 1
        #     temp = temp.next
        # pos = ListNodeLen - n + 1
        step = 0
        first = head
        second = dummy = ListNode(0, head) 
        while step != n:
            first = first.next
            step += 1
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next