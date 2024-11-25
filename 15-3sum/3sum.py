class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        left, right = 0, len(nums)
        result = []
        tracking_set = set()
        for index, value in enumerate(nums):
            first = value
            j = index +1
            k = len(nums)-1
            while j < k:
                three_sum = first + nums[j] + nums[k]
                if three_sum == 0:
                    key = str(first) + str(nums[j]) + str(nums[k])
                    if key not in tracking_set:
                        result.append([first, nums[j], nums[k]])
                        tracking_set.add(key)
                    j +=1
                    k-=1
                elif three_sum < 0:
                    j+=1
                else:
                    k-=1
        return result

