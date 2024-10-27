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
            if not current1 and not current2:
                return dummy.next
            elif not current1:
                new_node.next = ListNode(current2.val)
                current2 = current2.next
                new_node = new_node.next
            elif not current2:
                new_node.next = ListNode(current1.val)
                current1 = current1.next
                new_node = new_node.next
            else:
                val = current1.val if current1.val < current2.val else current2.val
                new_node.next = ListNode(val)
                new_node = new_node.next
                if current1.val < current2.val:
                    current1 = current1.next 
                else:
                    current2 = current2.next
        return dummy.next

        