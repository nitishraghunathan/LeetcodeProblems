# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    1. Check if the current node and next node is not None/empty
    2. Find the greates common divisor 
        1. Find the greatest common divisor
        2. check which ever node value is lessr and then divide it both and then keep lloking for all values < half the the lesser node 
    3. insert the greatest common divisor between the two nodes 
    """
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def greatest_common_divisor(val_one, val_two):
            if val_two > val_one:
                return greatest_common_divisor(val_two, val_one)
            if val_one%val_two == 0:
                return val_two
            gcd,i = 0, 1
            while i <= val_two//2:
                if val_two%i == 0 and val_one%i==0:
                    gcd = i
                i+=1
            return gcd           
        current = head
        dummy = head
        while current and current.next:
            new_val = greatest_common_divisor(current.val, current.next.val)
            new_node = ListNode(new_val)
            temp, current.next = current.next, new_node
            new_node.next = temp
            current = current.next.next
        current = dummy
        return current



        