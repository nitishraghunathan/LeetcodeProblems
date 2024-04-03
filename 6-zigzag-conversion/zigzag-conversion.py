class Solution:
    def convert(self, s: str, numRows: int) -> str:
        results = [[] for i in range(numRows)]
        index= 0
        flag = True
        if numRows < 2:
            return s
        for string in s:
            if flag:
                results[index].append(string)
                index +=1
                if index == numRows:
                    flag=False
                    index-=2
            else:
                results[index].append(string)
                index-=1
                if index == -1:
                    flag=True
                    index+=2
        return ''.join([''.join(result) for result in results])
        