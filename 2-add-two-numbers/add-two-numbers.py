# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        dummy = temp
        carry = 0
        sum_val = 0
        while l1 and l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0        
            temp.next = ListNode((carry + x +y)%10)
            temp =temp.next
            print(temp.val)
            carry = (x+y+carry)//10
            if l1:
                l1 =l1.next
            if l2:
                l2 =l2.next

        while l1:
            temp.next =ListNode((l1.val+carry)%10)
            temp =temp.next
            carry = (l1.val+carry)//10
            l1 = l1.next
        while l2:
            temp.next =ListNode((l2.val+carry)%10)
            temp =temp.next
            carry = (l2.val+carry)//10
            l2 = l2.next
        if carry:
            temp.next= ListNode(carry)
            temp =temp.next
        temp = dummy
        return temp.next
        
