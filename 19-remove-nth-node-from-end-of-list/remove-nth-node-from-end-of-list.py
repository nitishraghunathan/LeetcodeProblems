# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        slow = head
        for i in range(n):
            current = current.next
        if not current:
            return head.next
        while current.next:
            slow = slow.next
            current = current.next

        slow.next = slow.next.next
        return head

        