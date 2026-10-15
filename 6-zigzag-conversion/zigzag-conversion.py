class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        zig_zag = [[] for i in range(numRows)]
        counter = 0
        flag = False
        
        for i in s:
            print(f"counter: {counter}, flag: {flag}, i: {i}")
            zig_zag[counter] += i
            if not flag:
                counter +=1
            else:
                counter -=1
            if counter == numRows:
                flag = True
                counter-=2
            if counter == -1:
                flag = False
                counter+=2
        result = ""
        for i in zig_zag:
            for j in i:
                result += j 
        return result
        