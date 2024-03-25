# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth_node(current, k):
            while current and k > 0:
                current = current.next 
                k-=1
            return current
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = get_kth_node(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next 
            prev, current = kth.next, groupPrev.next
            while current != groupNext:
                temp = current.next 
                current.next = prev 
                prev = current 
                current =temp

            tmp = groupPrev.next   
            groupPrev.next = kth
            groupPrev = tmp  
        return dummy.next   