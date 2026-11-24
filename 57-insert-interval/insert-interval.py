import heapq
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        heapq.heapify(intervals)
        heapq.heappush(intervals,newInterval)
        result = []
        while len(intervals) > 1:
            first = heapq.heappop(intervals)
            second = heapq.heappop(intervals)
            if first[1] >= second[0]:
                heapq.heappush(intervals,[min(first[0], second[0]), max(first[1], second[1])])
            else:
                result.append(first)
                heapq.heappush(intervals,second)
        final = heapq.heappop(intervals)
        if result and result[-1][1] >= final[0]:
            result[-1][0] = min(final[0], result[-1][0])
            result[-1][1] = max(final[0], result[-1][1])
        else:
            result.append(final)
        return result


