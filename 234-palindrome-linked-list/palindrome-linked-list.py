# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        def reverse_list(node: ListNode | None):
            if not node:
                return node
            prev, current = None, node
            while current:
                next = current.next
                current.next = prev
                prev = current
                current = next
            return prev
        current, slow, fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = reverse_list(slow)
        while slow:
            if current.val != slow.val:
                return False
            current= current.next
            slow = slow.next
        return True

        