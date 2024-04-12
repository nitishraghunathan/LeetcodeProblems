class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])
        end_time = float('-inf')
        intervals_removed = 0
        for start, end in intervals:
            if start >= end_time:
                end_time = end
            else:
                intervals_removed+=1
        return intervals_removed
