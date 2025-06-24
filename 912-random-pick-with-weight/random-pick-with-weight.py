class Solution:

    def __init__(self, w: List[int]):
        self.total_sum = 0
        self.prefix_sum_list = []
        for weights in w:
            self.total_sum += weights
            self.prefix_sum_list.append(self.total_sum)
        

    def pickIndex(self) -> int:
        target = self.total_sum*random.random()
        left, right = 0, len(self.prefix_sum_list)-1
        while left < right:
            mid = left + (right-left)//2
            if self.prefix_sum_list[mid] < target:
                left = mid +1
            else:
                right =mid
        return left

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()