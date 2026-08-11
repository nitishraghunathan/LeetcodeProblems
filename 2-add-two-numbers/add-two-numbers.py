# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(-1)
        dummy = current
        carry = 0
        while l1 or l2:
            x, y = 0,0
            if l1:
                x= l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
            total_sum = (carry + x + y)
            unit_sum = total_sum%10
            carry  = total_sum//10
            current.next = ListNode(unit_sum)
            current = current.next
        if carry:
            current.next = ListNode(carry%10)
            carry = carry//10
            current = current.next
        return dummy.next

        