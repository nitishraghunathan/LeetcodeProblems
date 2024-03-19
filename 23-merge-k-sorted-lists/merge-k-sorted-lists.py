class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return ((self.value) < (other.value))
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        current = ListNode(-1)
        dummy = current
        queue = []
        heapq.heapify(queue)
        for index, linkedlist in enumerate(lists):
            if linkedlist is not None:
                heapq.heappush(queue, (linkedlist.val, index))
        while queue:
            val, index = heapq.heappop(queue)
            current.next = ListNode(val)
            current = current.next
            new_node = lists[index]
            if new_node:
                new_node = new_node.next
                lists[index] = new_node
                if new_node:
                    heapq.heappush(queue, (new_node.val, index))
        current = dummy
        return current.next
        