class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        1. Given a list of intervals, sort them based on the stat time
        2. check if any intervals overlap, if so add to the count
        """
        intervals = sorted(intervals, key=lambda x:x[1])
        end = intervals[0]
        minimum_intervals = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end[1]:
                minimum_intervals +=1
            else:
                end = intervals[i]
        return minimum_intervals