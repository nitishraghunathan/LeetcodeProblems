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
        queue = collections.deque()
        result = []
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])
        for i in range(k, len(nums)):
            if queue and queue[0]+k == i:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
        return result



            

