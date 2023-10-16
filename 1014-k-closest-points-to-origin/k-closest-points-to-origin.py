class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
         1. Since we are finding the distance form origin, we are going to assum/modify the formula to x^2 + y^2
         2. Iterate to through the array list and then add points and istance to athe queue which would be a min heap modified to a max heap computing the distance and converting to it negative and sorted based on the key
         3. Pop elements once size is greater the K
         4. return the coordinates
        """
        heap = []
        for point in points:
            distance = -((point[0]*point[0]) + (point[1]*point[1]))
            heapq.heappush(heap, (distance, point))
            if len(heap) > k:
                heapq.heappop(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]
