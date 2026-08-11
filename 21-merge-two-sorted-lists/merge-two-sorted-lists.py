# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(-1)
        dummy = current
        while l1 or l2:
            if l1 and l2:
                if l1.val > l2.val:
                    current.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    l1 = l1.next
            elif l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            current = current.next
        return dummy.next
                

        