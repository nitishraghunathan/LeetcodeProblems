class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                break
        low_index = i
        high_index = i
        while low_index > 0:
            if arr[low_index-1] >= arr[low_index]:
                return False
            low_index -=1 

        while high_index < len(arr)-1:
            if arr[high_index+1] >= arr[high_index]:
                return False
            high_index +=1 
        return low_index == 0 and high_index == len(arr)-1

        