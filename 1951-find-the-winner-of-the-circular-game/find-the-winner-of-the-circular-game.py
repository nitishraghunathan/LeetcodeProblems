class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result = [i+1 for i in range(n)]
        start = 0
        while len(result) > 1:
            start = (start + k-1)%len(result)
            result.pop(start)
        return result[0]
