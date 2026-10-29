class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # Create a dummy node to handle edge cases where the head itself is removed
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast forward n + 1 steps so that there is a gap of n between fast and slow
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Slow is now pointing to the node just before the one we want to delete
        slow.next = slow.next.next

        return dummy.next