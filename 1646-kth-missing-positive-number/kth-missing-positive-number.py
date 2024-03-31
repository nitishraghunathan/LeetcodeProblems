class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        new_arr = set(arr)
        counter = 1
        while True:
            if counter not in new_arr:
                k-=1
                if k==0:
                    return counter
            counter +=1