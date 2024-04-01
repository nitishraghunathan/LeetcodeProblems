class Solution:
    def countAndSay(self, n: int) -> str:
        def recursion(result):
            count = 1
            new_string = ''
            for index, number in enumerate(result):
                if index == len(result)-1 or result[index] != result[index+1]:
                    new_string += str(count) +result[index]
                    count = 1
                else:
                    count+=1
            return new_string

        result = '1'
        for i in range(2, n+1):
            result = recursion(result)
        return result