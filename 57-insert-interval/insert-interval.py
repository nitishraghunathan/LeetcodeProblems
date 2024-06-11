class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        intervals.append(newInterval)
        heapq.heapify(result)
        for interval in intervals:
            heapq.heappush(result, interval)
        interval = []
        while len(result) > 1:
            a = heapq.heappop(result)
            b = heapq.heappop(result)
            if a[1] >= b[0]:
                heapq.heappush(result, [min(a[0], a[1]), max(a[1],b[1])])
            else:
                interval.append(a)
                heapq.heappush(result, b)
        if len(result) > 0:
            if interval and interval[-1][1] >= result[-1][0]:
                interval[-1][1] = max(interval[-1][1], result[-1][1])
                interval[-1][0] = min(interval[-1][0], result[-1][0])
                heapq.heappop(result)
            else:
                interval.append(heapq.heappop(result))
        return interval


        