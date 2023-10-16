class KthLargest:
    """
    1. A queue would be required, this hsould be extended to min heap
    2. heapq would heapify after adding all the elements
    3. Once size is greater than K we pop the unrequired larger elements
    4. Return the head element fo the queue
    """

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.size = k
        heapq.heapify(self.queue)
        while len(self.queue) > self.size:
            heapq.heappop(self.queue)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        if len(self.queue) > self.size:
            heapq.heappop(self.queue)
        return self.queue[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)