class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        final_result = []
        for interval in intervals:
            heapq.heappush(result, [interval[0], interval[1]])
        heapq.heappush(result, [newInterval[0], newInterval[1]])
        while len(result) > 1:
            first = heapq.heappop(result)
            second = heapq.heappop(result)
            if second[0] > first[1]:
                final_result.append(first)
                heapq.heappush(result, second)
            else:
                heapq.heappush(result, [min(first[0], second[0]), max(first[1], second[1])])
        while result:
            first = heapq.heappop(result)
            if final_result:
                if first[0] > final_result[-1][1]:
                    final_result.append(first)
                else:
                    final_result.append(min(first[0], final_result[-1][0]), max(first[1], final_result[-1][1]))
            else:
                final_result.append(first)
        return final_result


        