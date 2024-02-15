class SparseVector:
    def __init__(self, nums: List[int]):
        self.map_dict = {}
        for index, value in enumerate(nums):
            if value != 0:
                self.map_dict[index] = value


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        product_sum = 0
        for key, value in self.map_dict.items():
            if key in vec.map_dict:
                product_sum += value*vec.map_dict[key]
        return product_sum
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)