"""
# Definition for an Interval.

"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        result=[]
        heapq.heapify(result)
        for sched in schedule:
            for interv in sched:
                print(interv)
                heapq.heappush(result, (interv.start, interv.end))
        free_interval = []
        while len(result) > 1:
            a= heapq.heappop(result)
            b= heapq.heappop(result)
            print(a)
            print(b)
            if b[0] <= a[1]:
                heapq.heappush(result, (min(a[0], b[0]), max(a[1], b[1])))
            else:
                free_interval.append(Interval(start=a[1], end=b[0]))
                heapq.heappush(result, b)
        if len(result) == 1:
            new_list= heapq.heappop(result)
            if free_interval and free_interval[-1].end < new_list[0]:
                free_interval.append(Interval(start=free_interval[-1].end, end=new_list[0]))
        return free_interval
        