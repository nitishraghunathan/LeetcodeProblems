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
        while l1 or l2 or carry > 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            sum_value = (carry+x+y)%10
            carry = (carry+x+y)//10
            new_node = ListNode(sum_value)
            current.next  = new_node
            current = current.next
        current = dummy
        return current.next