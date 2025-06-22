class MedianFinder:

    def __init__(self):
        """
        1. Have a large min heap for storing the larger elements in sorted 
        2. Have a small max heap for storing the smaller elements
        left - small_max_heap right - large_min_heap
        """
        self.large_min_heap = []
        self.small_max_heap = []

    def addNum(self, num: int) -> None:
        min_heap = self.large_min_heap
        max_heap = self.small_max_heap 
        heapq.heappush(max_heap, -1*num)
        if min_heap and max_heap and  min_heap[0] < -1 * max_heap[0]:
            heapq.heappush(min_heap, -1* heapq.heappop(max_heap))
        if len(min_heap) - len(max_heap) > 1:
            heapq.heappush(max_heap, -1 * heapq.heappop(min_heap))
        if len(max_heap) - len(min_heap) > 1:
            heapq.heappush(min_heap, -1 * heapq.heappop(max_heap))
        
    def findMedian(self) -> float:
        min_heap = self.large_min_heap
        max_heap = self.small_max_heap 
        if len(min_heap) == len(max_heap):
            return (min_heap[0] + (-1*max_heap[0]))/2
        elif len(min_heap) > len(max_heap):
            return float(min_heap[0])
        else:
            return -1 * float(max_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()