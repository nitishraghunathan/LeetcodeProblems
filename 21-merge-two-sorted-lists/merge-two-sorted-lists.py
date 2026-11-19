# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_node = ListNode(-1)
        tracker = new_node
        while list1 or list2:
            if not list1 or (list2 and list2.val < list1.val):
                new_node.next = list2
                list2 = list2.next
            elif not list2 or (list1 and list1.val <= list2.val):
                new_node.next = list1
                list1 = list1.next
            new_node = new_node.next
        new_node = tracker
        return tracker.next

        