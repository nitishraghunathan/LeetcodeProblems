class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset_list = []
        return self.recursion([],[],0,nums)
 
    
    def recursion(self, subset_list:List[List[int]], subset:List[int] , index:int, nums:List[int])-> List[List[int]]:
        if index == len(nums):
            subset_list.append(list(subset))
            return subset_list
        subset.append(nums[index])
        subset_list = self.recursion(subset_list, list(subset), index+1, nums)
        subset.pop()
        subset_list = self.recursion(subset_list,list(subset), index+1,nums)
        return subset_list
        
