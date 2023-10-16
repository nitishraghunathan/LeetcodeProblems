class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        """
        1. Stones need to be combined either by destroying them or taking the difference.
        2. If the stones have same weight they get destroyed else the difference remains
        3. Lets add the stones a queue and we compare the top 2 largest stones int eh queue.
        4. The comparison happens till we either get no stones a or a stone which can't be broken
        5. We would be using heapq for this problem
        """
        heapq.heapify(nums)
        while len(nums) > 1:
            result = heapq.nlargest(2,nums)
            nums.remove(result[0])
            nums.remove(result[1])
            if result[0] > result[1]:
                heapq.heappush(nums, result[0]-result[1])
        return nums.pop() if len(nums)>0 else 0