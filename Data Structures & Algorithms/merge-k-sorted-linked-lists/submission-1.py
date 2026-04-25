# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return
        # dummy = newHead = ListNode()
        # dummy.next = newHead
        # merged_list = []
        # for k in lists:
        #     temp = k
        #     while temp:
        #         merged_list.append(temp.val)
        #         temp = temp.next
        # for x in sorted(merged_list):
        #     newHead.next = ListNode(x)
        #     newHead = newHead.next
        # return dummy.next
        while len(lists) > 1:
            i = 0
            mergedLists = []
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
                i += 2
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = newHead = ListNode()
        dummy.next = newHead
        
        while l1 and l2:
            if l1.val < l2.val:
                newHead.next = ListNode(l1.val)
                l1 = l1.next
            else:
                newHead.next = ListNode(l2.val)
                l2 = l2.next
            newHead = newHead.next
        if l1:
            newHead.next = l1
        else:
            newHead.next = l2
        return dummy.next
          
        