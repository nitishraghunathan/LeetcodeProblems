class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        Algorithm: use DP memoization
        first take all the arrays, zip it and then sort it based on start time 
        use recursion to choose and not choose interval
        when we choose the next interval the startime should b greater than the end time of the current interval
        """
        intervals = sorted(zip(startTime, endTime, profit))
        dp = [-1]*len(intervals)
        def dfs(index, intervals, dp):
            if index == len(intervals):
                return 0
            if dp[index]!=-1:
                return dp[index]
            def binary_search(left, right, array, end_time):
                next_index = len(array)
                while left <=right:
                    mid = left + (right-left)//2
                    if intervals[mid][0] < end_time:
                        left = mid+1
                    else:
                        next_index = mid
                        right = mid-1
                return next_index
            new_index = binary_search(0, len(intervals)-1, intervals, intervals[index][1])
            result = max(dfs(index+1, intervals, dp), intervals[index][2] + dfs(new_index, intervals, dp))
            dp[index] = result
            return dp[index]
        return dfs(0, intervals,dp)
        