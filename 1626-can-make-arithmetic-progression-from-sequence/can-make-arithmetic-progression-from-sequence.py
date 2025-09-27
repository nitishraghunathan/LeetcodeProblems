class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = -1
        for index in range(1, len(arr)):
            if diff == -1:
                diff = arr[index] - arr[index-1]
                continue
            if arr[index] - arr[index-1] != diff:
                return False
        return True
        