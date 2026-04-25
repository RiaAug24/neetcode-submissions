# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = 0
        head1, head2 = l1, l2
        while head1:
            num1 = num1 * 10 + head1.val
            head1 = head1.next

        while head2:    
            num2 = num2 * 10 + head2.val
            head2 = head2.next
       
        rev_num1 = rev_num2 = 0
        num1_str, num2_str = str(num1), str(num2)

        for i in range(len(num1_str) - 1, -1, -1):
            rev_num1 = rev_num1 * 10 + int(num1_str[i])

        for i in range(len(num2_str) - 1, -1, -1):
            rev_num2 = rev_num2 * 10 + int(num2_str[i])

        res = str(rev_num1 + rev_num2)
        print(res)
        dummy = ListNode()
        newHead = ListNode()
        dummy.next = newHead
        for i in range(len(res) -1 , -1 , -1):
            newHead.next = ListNode()
            newHead = newHead.next
            newHead.val = int(res[i])
        return dummy.next.next
        




        
        