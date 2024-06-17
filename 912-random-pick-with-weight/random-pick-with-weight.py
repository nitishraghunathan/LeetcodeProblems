class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        create a prefix sum:
        add all the weights and store prefix sum array 
        have a total_sum array 
        when comupting weighted random 
        use total_sum * random.random 
        ince you get the weight 
        find the index closest to the weight 
        use low = 0 and high = len(w)-1
        and then if target < w[mid] reduce the right window else 
        increase the left window
        """
        #Accumulate all the wieghts and find the index closest to the weight
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        target = self.total_sum * random.random()
        # run a binary search to find the target zone
        low, high = 0, len(self.prefix_sums)
        while low < high:
            mid = low + (high - low) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()