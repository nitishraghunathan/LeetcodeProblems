class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Thought process
        recursion:
        1. Base condition if index > len(nums)-1 add it to the result and return
        2. Have a for loop which interates through all elements in number
        3. Either pick one and perform recursion or dont add and perform recursion.
        4. increase the index by one for every recursive call
        """
        result = set()
        def recursion(nums:list, target_list:list, index:int):
            if index > len(nums) - 1:
                result.add(tuple(target_list))
                return
            for i in range(index, len(nums)):
                target_list.append(nums[i])
                recursion(nums, target_list, i+1)
                target_list.pop()
                recursion(nums, target_list, i+1)
            return 
        recursion(nums, [], 0)
        return list(result)