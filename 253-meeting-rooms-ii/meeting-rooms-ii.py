class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        """
        sort all the rooms based on intervals start time
        add the first meeting room 
        1. compare all the intervals start time with the end time of peek element in the queue
        2. if end time start time is less than end time push it to the queue else pop it off
        """
        intervals = sorted(intervals, key = lambda x:x[0])
        results = []
        heapq.heappush(results, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= results[0]:
                heapq.heappop(results)
            heapq.heappush(results, intervals[i][1])
        return len(results)


            