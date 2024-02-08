class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        for index, interval in enumerate(intervals):
            if index < len(intervals) -1:
                if intervals[index][1] > intervals[index+1][0]:
                    return False
        return True

