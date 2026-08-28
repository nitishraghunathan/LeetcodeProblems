# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, current = None, slow
        while current:
            next = current.next
            current.next = prev
            prev = current
            current  = next
        first, slow = head, prev
        while slow:
            if slow.val != first.val:
                return False
            slow = slow.next
            first = first.next 
        return True