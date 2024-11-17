class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for point in points:
            heapq.heappush(result, (-(point[0]*point[0] + point[1]*point[1]), point))
        while len(result) > k:
            heapq.heappop(result)
        return [point[1] for point in result]
        