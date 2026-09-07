class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > third:
                first, second, third = second, third, num
            elif num < third and num > second:
                first, second = second, num
            elif num < second and num > first:
                first = num
        if first > float('-inf'):
            return first
        return third
        