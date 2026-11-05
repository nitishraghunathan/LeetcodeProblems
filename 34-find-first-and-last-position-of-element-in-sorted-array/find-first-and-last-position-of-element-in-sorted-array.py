class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(nums: list[int], second_run: bool, target: int):
            left, right, tar = 0, len(nums)-1, False
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    tar = True
                    if second_run:
                        left = mid+1
                    else:
                        right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            if not tar:
                return -1
            return right if second_run else left
        return [binary_search(nums, False, target), binary_search(nums, True, target)]


        