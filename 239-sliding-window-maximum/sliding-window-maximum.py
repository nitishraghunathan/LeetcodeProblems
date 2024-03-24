class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Use a double ended queue.
        store all indices in the queue and remove all small elements at top of the queue which are less than the current element
        append the element tp the queue
        check if first element in queue is out of bounds, if yes pop it off.
        now check if the sliding window is intact, if yes add left most element in the queue 
        increase left pointer.
        """
        left, right, end = 0,0, len(nums)
        queue = collections.deque()
        result = []
        while right < end:
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop() 
            queue.append(right)
            if left > queue[0]:
                queue.popleft()
            if right + 1 >= k:
                result.append(nums[queue[0]])
                left+=1
            right+=1
        return result



            

