class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        outputs = []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            outputs.append(intervals[i])
            i += 1
        
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        outputs.append(newInterval)

        while i < len(intervals):
            outputs.append(intervals[i])
            i += 1
        
        return outputs