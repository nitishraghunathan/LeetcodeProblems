class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        These are the cocepts we need to be mindful of
        1. Binary Search
        2. Dynamic Programming
        3. Recursion
        1 - Get a list of lists having start_time, end_time, profit
        2. Use recursion to interate every job, we should use choice based recursion,
        we pick the job anfd ctake the next job whose start time is greater than end time
        else we don't pick and find the next job. we compuet the max profit for both
        3. Return the max profit
        """
        intervals = sorted(zip(startTime, endTime, profit))
        dp = [-1]*len(startTime)
        def dfs(index):
            if index == len(startTime):
                return 0
            if dp[index] != -1:
                return dp[index]
            def binary_search(left, right, endTime):
                index = len(startTime)
                while left <= right:
                    mid = left + (right-left)//2
                    if intervals[mid][0] < endTime:
                        left = mid +1
                    else:
                        right = mid -1
                        index = mid 
                return index
            new_index = binary_search(index, len(startTime)-1, intervals[index][1])
            result = max(dfs(index+1), intervals[index][2] + dfs(new_index))
            dp[index] = result
            return dp[index]
        return dfs(0)
        