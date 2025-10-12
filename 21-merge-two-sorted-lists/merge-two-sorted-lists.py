# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        new_list = ListNode(-1)
        dummy = new_list
        while current1 or current2:
            x = current1.val if current1 else float('inf')
            y = current2.val if current2 else float ('inf')
            if x  == float('inf'):
                new_list.next = current2
                current2 = current2.next
            elif y == float('inf'):
                new_list.next = current1
                current1 = current1.next
            elif x >= y:
                new_list.next = current2
                current2 = current2.next
            else:
                new_list.next = current1
                current1 = current1.next
            new_list = new_list.next
        new_list = dummy
        return new_list.next


        