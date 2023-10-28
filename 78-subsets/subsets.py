class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = []
        return self.recursion([],[],0,nums)
 
    
    def recursion(self, subset_list:List[List[int]], subset:List[int] , index:int, nums:List[int])-> List[List[int]]:
        if index == len(nums):
            subset_list.append(subset.copy())
            return subset_list
        subset_list = self.recursion(subset_list,subset, index+1,nums)
        copy = subset.copy()
        copy.append(nums[index])
        subset_list = self.recursion(subset_list, copy, index+1, nums)
        return subset_list
        
