class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        queue = []
        for num in nums:
            heapq.heappush(queue, int(num))
            if len(queue) > k:
                heapq.heappop(queue)
        return str(queue[0])