class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = []
        for ar in arr:
            heapq.heappush(result, (-abs(ar - x), -ar))
            if len(result) > k:
                heapq.heappop(result)
            size = len(result)
        return sorted([-heapq.heappop(result)[1] for i in range(size)])