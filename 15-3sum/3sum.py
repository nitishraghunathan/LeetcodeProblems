class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        first = 0
        final_pointer = len(nums)
        result = set()
        nums = sorted(nums)
        while first < final_pointer:
            second = first+1
            third = final_pointer-1
            while second < final_pointer and third < final_pointer and second < third:
                total_sum = nums[second] + nums[third] + nums[first]
                if total_sum == 0:
                    result.add((nums[first], nums[second], nums[third]))
                    second +=1
                    third -=1
                elif total_sum < 0:
                    second+= 1
                else:
                    third-= 1
            first +=1
        return [[arr[0], arr[1], arr[2]] for arr in result]