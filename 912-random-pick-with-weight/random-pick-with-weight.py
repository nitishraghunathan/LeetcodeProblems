class Solution:

    def __init__(self, w: List[int]):
        self.prefix_total_sum = []
        self.prefix_sum = 0
        for weights in w:
            self.prefix_sum += weights
            self.prefix_total_sum.append(self.prefix_sum)


    def pickIndex(self) -> int:

        target = self.prefix_sum*random.random()
        low, high = 0, len(self.prefix_total_sum)
        while low < high:
            mid = low + (high-low)//2
            if self.prefix_total_sum[mid] < target:
                low = mid+1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()