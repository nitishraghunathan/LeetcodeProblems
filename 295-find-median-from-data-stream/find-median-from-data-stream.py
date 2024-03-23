class MedianFinder:

    def __init__(self):
        self.large_elements_min_heap = []
        self.small_elements_max_heap = []
        heapq.heapify(self.large_elements_min_heap)
        heapq.heapify(self.small_elements_max_heap)
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_elements_max_heap, -1*num)
        if self.large_elements_min_heap and self.small_elements_max_heap and self.small_elements_max_heap[0]*-1 > self.large_elements_min_heap[0]:
            heapq.heappush(self.large_elements_min_heap, -1*heapq.heappop(self.small_elements_max_heap))
        if len(self.large_elements_min_heap) > len(self.small_elements_max_heap) +1:
            heapq.heappush(self.small_elements_max_heap, -1* heapq.heappop(self.large_elements_min_heap))
        if len(self.small_elements_max_heap) > len(self.large_elements_min_heap) +1:
            heapq.heappush(self.large_elements_min_heap, -1*heapq.heappop(self.small_elements_max_heap))
    def findMedian(self) -> float:
        if len(self.small_elements_max_heap) > len(self.large_elements_min_heap):
            return float(-1*self.small_elements_max_heap[0])
        if len(self.large_elements_min_heap) > len(self.small_elements_max_heap):
            return float(self.large_elements_min_heap[0])

        return ((self.small_elements_max_heap[0]*-1) + self.large_elements_min_heap[0])/2
        
        


# Your MedianFinder object will be instantiated and called as such:
"""
In order to optimize this we need to solve in log(n) team for addition to a queue
but median of a queue is retrieved in o(1) time 
hence better to use priority queue
"""
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()