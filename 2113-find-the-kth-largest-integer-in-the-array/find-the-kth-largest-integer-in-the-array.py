class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """
        1. heap queue is intiutive to this problem.
        2. We add elements to the queue and we pop them if the size > k
        3. return the head of the queue
        """
        queue = []
        for num in nums:
            heapq.heappush(queue, int(num))
            if len(queue) > k:
                heapq.heappop(queue)
        return str(queue[0])
        