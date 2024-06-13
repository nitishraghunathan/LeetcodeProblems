class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result= []
        def recursion(nums, new_list, index):
            if index == len(nums):
                result.append(list(new_list))
                return 
            new_list.append(nums[index])
            recursion(nums, new_list, index+1)
            new_list.pop()
            recursion(nums, new_list, index+1)
            return
        recursion(nums,[],0)
        return result