class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = firstList + secondList
        heapq.heapify(result)
        outcome = []
        while len(result) > 1:
            a = heapq.heappop(result)
            b = heapq.heappop(result)
            if b[0] <= a[1]:
                outcome.append([max(a[0], b[0]), min(a[1], b[1])])
            heapq.heappush(result, [b[0], max(a[1], b[1])])
        return outcome


