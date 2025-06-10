class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[0])
        results = []
        heapq.heappush(results, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= results[0]:
                heapq.heappop(results)
            heapq.heappush(results, intervals[i][1])
        return len(results)