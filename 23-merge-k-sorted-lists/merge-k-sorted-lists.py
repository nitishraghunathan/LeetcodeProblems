

        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        for index, list_node in enumerate(lists):
            if list_node:
                heapq.heappush(queue, (list_node.val, index))
        dummy = ListNode(-1)
        current = dummy
        while queue:
            val, index = heapq.heappop(queue)
            new_node = ListNode(val)
            current.next = new_node
            current = current.next
            added_node = lists[index]
            added_node = added_node.next
            lists[index] = added_node
            if added_node:
                heapq.heappush(queue, (added_node.val, index))
        current = dummy
        return current.next
            

        

        