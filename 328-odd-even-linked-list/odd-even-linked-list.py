# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_odd = ListNode(-1)
        node_even = ListNode(-1)
        copy_one = node_odd
        copy_two = node_even
        if not head or not head.next:
            return head
        current = head
        counter = 0
        while current.next:
            temp = current.next
            current.next = current.next.next
            temp.next = None
            if counter%2==1:
                node_odd.next = temp 
                node_odd = node_odd.next
            else:
                node_even.next = temp 
                node_even = node_even.next
            counter +=1
        node_even = copy_two.next
        node_odd.next = node_even
        node_odd = copy_one.next
        head.next = node_odd
        return head


        