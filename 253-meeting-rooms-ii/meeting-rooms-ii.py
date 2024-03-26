class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        """
        sort all the rooms based on intervals start time
        add the first meeting room 
        1. compare all the intervals start time with the end time of peek element in the queue
        2. if end time start time is less than end time push it to the queue else pop it off
        """
        counter = 0
        temp = None
        if not intervals:
            return 0
        intervals= sorted(intervals, key=lambda value:value[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)



            