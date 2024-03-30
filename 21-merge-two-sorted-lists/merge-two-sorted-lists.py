# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode(-1)
        dummy =current
        if not list1:
            return list2
        if not list2:
            return list1
        while list1 and list2:
            if list1.val > list2.val:
                temp= ListNode(list2.val)
                dummy.next = temp
                list2 = list2.next
                
            else:
                temp = ListNode(list1.val)
                list1 = list1.next
                dummy.next = temp
            dummy = dummy.next
     
        if list1:
            dummy.next = list1

        if list2:
            dummy.next = list2

        
        # current = dummy 
        return current.next

