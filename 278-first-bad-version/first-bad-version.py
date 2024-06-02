# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = low + (high-low)//2
            if not isBadVersion(mid) and isBadVersion(mid+1):
                return mid+1
            elif not isBadVersion(mid):
                low = mid+1
            else:
                high = mid -1
        return low