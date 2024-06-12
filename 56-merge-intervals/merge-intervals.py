class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        queue = []
        for interval in intervals:
            heapq.heappush(queue, interval)
        result = []
        while len(queue) > 1:
            a = heapq.heappop(queue)
            b = heapq.heappop(queue)
            if b[0] <= a[1]:
                heapq.heappush(queue, [min(a[0],b[0]), max(a[1],b[1])])
            else:
                result.append(a)
                heapq.heappush(queue, b)
        print(result)
        print(queue)
        if len(queue) > 0:
            if result and result[-1][1] >= queue[-1][0]:
                result[-1][0] = min(result[-1][0], queue[-1][0])
                result[-1][1] = max(result[-1][1], queue[-1][1])
            else:
                result.append(heapq.heappop(queue))
        return result


            