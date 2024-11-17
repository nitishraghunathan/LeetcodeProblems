class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heapq.heapify(intervals)
        result = []
        heapq.heappush(intervals, newInterval)
        while len(intervals) > 1:
            first = heapq.heappop(intervals)
            second = heapq.heappop(intervals)
            if first[1] >= second[0]:
                heapq.heappush(intervals, [min(first[0], second[0]), max(first[1], second[1])])
            else:
                result.append(first)
                heapq.heappush(intervals, second)
        if len(intervals):
            last = heapq.heappop(intervals)
            if result and last[0] <= result[-1][1]:
                result[-1][0] = min(result[-1][0], last[0])
                result[-1][1] = max(result[-1][1], last[1])
            else:
                result.append(last)
        return result

        