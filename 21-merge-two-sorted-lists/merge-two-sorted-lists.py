class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        # Attach whichever list still has remaining nodes
        curr.next = list1 if list1 else list2

        return dummy.next