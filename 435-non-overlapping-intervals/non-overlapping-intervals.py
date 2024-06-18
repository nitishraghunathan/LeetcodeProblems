class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,  key = lambda x:x[1])
        ending = float('-inf')
        result = 0
        print(intervals)
        for index,value in enumerate(intervals):
            if value[0] >= ending:
                ending = value[1]
            else:
                result +=1
        return result