class NumArray:

    def __init__(self, nums: List[int]):
        self.map_dict = {}
        total_sum = 0
        for index, value in enumerate(nums):
            if index not in self.map_dict:
                self.map_dict[index] = total_sum
            total_sum += value
        self.map_dict[len(nums)] = total_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.map_dict[right+1] - self.map_dict[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)