class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.large_min_heap = []
        heapq.heapify(self.small_max_heap)
        heapq.heapify(self.large_min_heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max_heap, -1*num)
        if self.small_max_heap and self.large_min_heap and -1*self.small_max_heap[0] > self.large_min_heap[0]:
            heapq.heappush(self.large_min_heap, -1*heapq.heappop(self.small_max_heap))
        if len(self.small_max_heap) -len(self.large_min_heap) > 1:
            heapq.heappush(self.large_min_heap, -1*heapq.heappop(self.small_max_heap))
        if len(self.large_min_heap) -len(self.small_max_heap) > 1:
            heapq.heappush(self.small_max_heap, -1*heapq.heappop(self.large_min_heap))

        

    def findMedian(self) -> float:
        if len(self.large_min_heap) == len(self.small_max_heap):
            return ((self.small_max_heap[0]*-1) + self.large_min_heap[0])/2
        return float(self.small_max_heap[0]*(-1)) if len(self.small_max_heap) > len(self.large_min_heap) else float(self.large_min_heap[0])



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()