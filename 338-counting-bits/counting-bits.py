class Solution:
    def countBits(self, n: int) -> List[int]:
        def number_of_ones(counter):
            count = 0
            while counter > 0:
                count += 1 if counter%2==1 else 0
                counter = counter//2
            return count
        return [number_of_ones(i) for i in range(n+1)]

        