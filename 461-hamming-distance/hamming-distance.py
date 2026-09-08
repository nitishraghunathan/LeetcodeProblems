class Solution:
    def hammingDistance(self, x, y):
        def binary(number: int):
            result = ""
            while number > 0:
                if number % 2 == 0:
                    result = "0" + result 
                else:
                    result = "1" + result 
                number = number // 2
            return result

        def append_num(number, diff):
            for i in range(diff):
                number = "0" + number
            return number

        first, second = binary(x), binary(y)
        diff = abs(len(first) - len(second))
        if len(first) > len(second):
            second = append_num(second, diff)
        elif len(second) > len(first):
            first = append_num(first, diff)
        counter = 0
        for i in range(len(first)):
            if first[i] != second[i]:
                counter +=1
        return counter


            