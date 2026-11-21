class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        prev = None
        for interval in intervals:
            if prev and interval[0] < prev[1]:
                return False
            prev = interval
        return True
            
        