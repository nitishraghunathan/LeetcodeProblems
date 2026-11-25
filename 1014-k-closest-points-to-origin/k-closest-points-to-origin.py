import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        queue = []
        result = []
        for point in points:
            heapq.heappush(queue, [-(point[0]*point[0]+ point[1]*point[1]), -point[0],-point[1]])
            if len(queue) > k:
                heapq.heappop(queue)
        while len(queue) > 0:
            c, a, b =heapq.heappop(queue)
            result.append([-a, -b])
        return result


