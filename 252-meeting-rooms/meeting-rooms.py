class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        temp = None
        for interval in intervals:
            if temp:
                if interval[0] < temp[1]:
                    return False
            temp = interval
        return True
        

        