# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(-1)
        dummy = new_list
        total_sum = 0
        carry = 0
        while l1 or l2 or carry:
            if l1:
                x = l1.val
                l1 = l1.next
            else:
                x = 0
            if l2: 
                y = l2.val
                l2 = l2.next
            else:
                y = 0
            total_sum = (x + y + carry)%10
            carry = (x + y + carry)//10
            new_list.next = ListNode(total_sum)
            new_list = new_list.next
        new_list = dummy
        return new_list.next

            

        