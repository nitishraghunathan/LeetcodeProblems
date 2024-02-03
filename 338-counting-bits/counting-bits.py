class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            binary = bin(i)
            count = 0
            for j in binary:
                if j == '1':
                    count +=1
            result.append(count)
        return result