# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        new_node = ListNode(-1)
        dummy = new_node
        while current1 or current2:
            x = 0 if not current1 else current1.val
            y = 0 if not current2 else current2.val
            if not current1:
                new_node.next = ListNode(y)
                current2 = current2.next

            elif not current2:
                new_node.next = ListNode(x)
                current1 = current1.next
            elif x > y:
                new_node.next = ListNode(y)
                if current2:
                    current2 = current2.next
            else:
                new_node.next = ListNode(x)
                if current1:
                    current1 = current1.next
            new_node = new_node.next
        return dummy.next

        