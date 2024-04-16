class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_dict = {}
        for index, value in enumerate(nums):
            if target - value in two_dict:
                return [two_dict[target-value], index]
            else:
                two_dict[value] = index
        return [-1,-1]