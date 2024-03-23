class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        heapq.heapify(intervals)
        result = []
        original_length = len(intervals)
        while len(intervals) > 1:
            first = heapq.heappop(intervals)
            second = heapq.heappop(intervals)
            if second[0] >= first[1]:
                heapq.heappush(intervals, second)
            else:
                if second[1] > first[1]:
                    result.append((second[0], second[1]))
                    heapq.heappush(intervals, first)
                else:
                    result.append((first[0], first[1]))
                    heapq.heappush(intervals, second)
                    
        return len(result)

