class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        1. initialize a queue which would be a minheap
        2. Add all elements from nums to queue
        3. We pop elements if size is greater than k
        4. return the head of the queue
        """
        queue = []
        for num in  nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)
        return queue[0]