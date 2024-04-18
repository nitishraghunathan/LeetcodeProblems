class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >=nums[low]:
                if target < nums[mid] and target >= nums[low]:
                    high = mid -1
                else:
                    low = mid +1
            else:
                if nums[mid] < target and target <=nums[high]:
                    low = mid +1
                else:
                    high = mid -1
        return -1
                
        